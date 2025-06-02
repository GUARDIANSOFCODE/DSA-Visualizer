import tkinter as tk
import time
import random

def draw(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    for i, height in enumerate(data):
        x0 = i * x_width
        y0 = c_height - height
        x1 = (i + 1) * x_width
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
    root.update_idletasks()

def bubble_sort():
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                draw(data, ["green" if x == j or x == j+1 else "gray" for x in range(len(data))])
                time.sleep(0.1)
    draw(data, ["green"] * len(data))

def start_sort():
    global data
    data = [random.randint(10, 350) for _ in range(30)]
    draw(data, ["gray"] * len(data))

root = tk.Tk()
root.title("Bubble Sort Visualizer")
canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack()

start_button = tk.Button(root, text="Generate & Sort", command=lambda: [start_sort(), bubble_sort()])
start_button.pack()

root.mainloop()
