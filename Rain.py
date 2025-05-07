import random
import shutil
import time
import os

def matrix_rain():
    columns, rows = shutil.get_terminal_size()
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    drops = [0 for _ in range(columns)]

    try:
        while True:
            print("\033[1;32m", end='')  
            for i in range(columns):
                if random.random() > 0.975:
                    print(random.choice(chars), end='')
                    drops[i] = 0
                else:
                    print(' ', end='')
            print()

            for i in range(len(drops)):
                drops[i] += 1
                if drops[i] > rows:
                    drops[i] = 0

            time.sleep(0.05)
            os.system('cls' if os.name == 'nt' else 'clear')
    except KeyboardInterrupt:
        print("\033[0m")  
        print("Matrix rain stopped.")

matrix_rain()
