import turtle
import colorsys

def colorful_spiral():
    t = turtle.Turtle()
    turtle.bgcolor("black")
    t.speed(0)
    t.width(2)

    num_colors = 36
    hue = 0

    for i in range(360):
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        t.pencolor(color)
        t.forward(i * 3 / num_colors + i)
        t.left(59)
        t.circle(i * 0.1, 60)
        hue += 1 / num_colors

    turtle.done()

colorful_spiral()
