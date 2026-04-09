import tkinter as tk
import random
import time

# window
root = tk.Tk()
root.title("DSA Visualizer")
root.geometry("900x650")

data = []

# canvas
canvas = tk.Canvas(root, width=850, height=400, bg="white")
canvas.pack(pady=20)

# speed slider (faster)
speed_scale = tk.Scale(
    root,
    from_=0.001,
    to=0.05,
    resolution=0.001,
    digits=3,
    length=200,
    orient=tk.HORIZONTAL,
    label="Speed"
)
speed_scale.set(0.005)
speed_scale.pack()

def get_speed():
    return speed_scale.get()


# draw bars
def draw_data(data, color):
    canvas.delete("all")
    width = 850 / len(data)

    for i, value in enumerate(data):
        x0 = i * width
        y0 = 400 - value
        x1 = (i + 1) * width
        y1 = 400

        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])

    root.update_idletasks()


# generate array
def generate():
    global data
    data = [random.randint(20, 380) for _ in range(40)]
    draw_data(data, ["blue"] * len(data))


# -----------------
# Bubble Sort
# -----------------
def bubble_sort():
    n = len(data)

    for i in range(n):
        for j in range(n - i - 1):

            colors = ["blue"] * len(data)
            colors[j] = "red"
            colors[j+1] = "red"

            draw_data(data, colors)
            time.sleep(get_speed())

            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    draw_data(data, ["green"] * len(data))


# -----------------
# Selection Sort
# -----------------
def selection_sort():
    n = len(data)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):

            colors = ["blue"] * len(data)
            colors[min_index] = "red"
            colors[j] = "yellow"

            draw_data(data, colors)
            time.sleep(get_speed())

            if data[j] < data[min_index]:
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]

    draw_data(data, ["green"] * len(data))


# -----------------
# Merge Sort
# -----------------
def merge_sort():
    merge_sort_recursive(data, 0, len(data)-1)
    draw_data(data, ["green"] * len(data))


def merge_sort_recursive(arr, left, right):
    if left < right:

        mid = (left + right) // 2

        merge_sort_recursive(arr, left, mid)
        merge_sort_recursive(arr, mid+1, right)

        merge(arr, left, mid, right)


def merge(arr, left, mid, right):

    left_part = arr[left:mid+1]
    right_part = arr[mid+1:right+1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):

        colors = ["blue"] * len(arr)
        colors[k] = "red"

        draw_data(arr, colors)
        time.sleep(get_speed())

        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1

        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


# -----------------
# Quick Sort
# -----------------
def quick_sort():
    quick_sort_recursive(0, len(data)-1)
    draw_data(data, ["green"] * len(data))


def quick_sort_recursive(low, high):
    if low < high:
        pivot = partition(low, high)

        quick_sort_recursive(low, pivot-1)
        quick_sort_recursive(pivot+1, high)


def partition(low, high):

    pivot = data[high]
    i = low - 1

    for j in range(low, high):

        colors = ["blue"] * len(data)
        colors[j] = "yellow"
        colors[high] = "red"

        draw_data(data, colors)
        time.sleep(get_speed())

        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]

    data[i+1], data[high] = data[high], data[i+1]

    return i+1


# buttons
frame = tk.Frame(root)
frame.pack(pady=20)

tk.Button(frame, text="Generate Array", command=generate).grid(row=0, column=0, padx=10)
tk.Button(frame, text="Bubble Sort", command=bubble_sort).grid(row=0, column=1, padx=10)
tk.Button(frame, text="Selection Sort", command=selection_sort).grid(row=0, column=2, padx=10)
tk.Button(frame, text="Merge Sort", command=merge_sort).grid(row=0, column=3, padx=10)
tk.Button(frame, text="Quick Sort", command=quick_sort).grid(row=0, column=4, padx=10)

root.mainloop()