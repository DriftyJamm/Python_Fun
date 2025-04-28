import tkinter as tk
from tkinter import ttk
import requests
import time
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

API_KEY = 'AsqXD6Y1OTleolBrI9jeMz'

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def update_weather():
    city = city_entry.get()
    data = get_weather_data(city)

    if data['cod'] == 200:
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        icon_code = data['weather'][0]['icon']

        weather_label.config(text=f"{temp}°C, {description.capitalize()}")
        humidity_label.config(text=f"Humidity: {humidity}%")

        icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
        icon_img = Image.open(requests.get(icon_url, stream=True).raw)
        icon_img = icon_img.resize((50, 50))
        icon_photo = ImageTk.PhotoImage(icon_img)
        icon_label.config(image=icon_photo)
        icon_label.image = icon_photo

        plot_weather_graphs(data)
    else:
        weather_label.config(text="City not found.")
        humidity_label.config(text="")
        icon_label.config(image="")
        icon_label.image = None

def plot_weather_graphs(data):
    times = [datetime.utcfromtimestamp(dt).strftime('%H:%M') for dt in data['hourly']['time']]
    temps = data['hourly']['temperature_2m']
    humidities = data['hourly']['relative_humidity_2m']

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

    ax1.plot(times, temps, label='Temperature (°C)', color='tab:red')
    ax1.set_title('Temperature Over Time')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Temperature (°C)')
    ax1.grid(True)

    ax2.plot(times, humidities, label='Humidity (%)', color='tab:blue')
    ax2.set_title('Humidity Over Time')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Humidity (%)')
    ax2.grid(True)

    for ax in [ax1, ax2]:
        ax.set_xticks(times[::2])
        ax.set_xticklabels(times[::2], rotation=45)

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def update_time():
    current_time = time.strftime('%H:%M:%S')
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

root = tk.Tk()
root.title("Weather Dashboard")

time_label = tk.Label(root, font=('Helvetica', 24))
time_label.pack()

city_entry = tk.Entry(root, font=('Helvetica', 14))
city_entry.pack(pady=10)

weather_label = tk.Label(root, font=('Helvetica', 16))
weather_label.pack()

humidity_label = tk.Label(root, font=('Helvetica', 14))
humidity_label.pack()

icon_label = tk.Label(root)
icon_label.pack()

graph_frame = tk.Frame(root)
graph_frame.pack(pady=20)

fetch_button = tk.Button(root, text="Get Weather", command=update_weather, font=('Helvetica', 14))
fetch_button.pack()

update_time()
root.mainloop()
