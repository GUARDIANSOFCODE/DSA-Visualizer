import tkinter as tk
from tkinter import ttk
import random
import time

# Sorting Algorithms
def bubble_sort(data, draw_data, speed):
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                draw_data(data, ['red' if x == j or x == j+1 else 'blue' for x in range(len(data))])
                time.sleep(speed)
    draw_data(data, ['green' for x in range(len(data))])

def insertion_sort(data, draw_data, speed):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >=0 and key < data[j]:
            data[j + 1] = data[j]
            draw_data(data, ['red' if x == j or x == j+1 else 'blue' for x in range(len(data))])
            time.sleep(speed)
            j -= 1
        data[j + 1] = key
    draw_data(data, ['green' for x in range(len(data))])

# Draw function
def draw_data(data, color_array):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 10
    spacing = 5

    normalized_data = [i / max(data) for i in data]
    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset
        y0 = c_height - height * 350
        x1 = (i + 1) * x_width
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
        canvas.create_text(x0+2, y0, anchor=tk.SW, text=str(data[i]), font=("Arial", 8))

    root.update_idletasks()

# Generate Data
def generate_data():
    global data
    data = [random.randint(10, 100) for _ in range(int(size_entry.get()))]
    draw_data(data, ['blue' for x in range(len(data))])

# Start Sorting
def start_sort():
    global data
    speed = speed_scale.get()
    algo = algo_menu.get()

    if algo == 'Bubble Sort':
        bubble_sort(data, draw_data, speed)
    elif algo == 'Insertion Sort':
        insertion_sort(data, draw_data, speed)

# GUI
root = tk.Tk()
root.title("DSA Sorting Visualizer")
root.maxsize(700, 500)
root.config(bg="white")

algo_menu = tk.StringVar()
algo_menu.set("Bubble Sort")

data = []

# UI Frame
ui_frame = tk.Frame(root, width=600, height=200, bg="lightgrey")
ui_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = tk.Canvas(root, width=600, height=380, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)

# UI Elements
tk.Label(ui_frame, text="Algorithm:", bg="lightgrey").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
algo_dropdown = ttk.Combobox(ui_frame, textvariable=algo_menu, values=['Bubble Sort', 'Insertion Sort'])
algo_dropdown.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ui_frame, text="Size:", bg="lightgrey").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
size_entry = tk.Entry(ui_frame)
size_entry.insert(0, "30")
size_entry.grid(row=0, column=3, padx=5, pady=5)

tk.Label(ui_frame, text="Speed (s):", bg="lightgrey").grid(row=0, column=4, padx=5, pady=5, sticky=tk.W)
speed_scale = tk.Scale(ui_frame, from_=0.01, to=1.0, length=100, digits=3, resolution=0.01, orient=tk.HORIZONTAL)
speed_scale.set(0.1)
speed_scale.grid(row=0, column=5, padx=5, pady=5)

tk.Button(ui_frame, text="Generate", command=generate_data, bg="green", fg="white").grid(row=1, column=0, padx=5, pady=5)
tk.Button(ui_frame, text="Sort", command=start_sort, bg="blue", fg="white").grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
