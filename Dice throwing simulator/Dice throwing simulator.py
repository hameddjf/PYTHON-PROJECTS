import tkinter as tk
import random

root = tk.Tk()
root.title("شبیه ساز پرتاپ تاس")

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

def create_circle(x, y, r, **kwargs):
    return canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

def roll_dice():
    canvas.delete("all")

    # Draw the dice
    canvas.create_rectangle(50, 50, 250, 250, fill="white")
    # create_circle(100, 100, 20, fill="black")
    # create_circle(200, 200, 20, fill="black")

    # Roll the dice and draw the result
    result = random.randint(1 , 6)
    print(result)
    if result == 1:
        create_circle(150, 150, 20, fill="black")
    if result == 2:
        create_circle(100, 100, 20, fill="black")
        create_circle(200, 200, 20, fill="black")
    if result == 3:
        create_circle(100, 100, 20, fill="black")
        create_circle(150, 150, 20, fill="black")
        create_circle(200, 200, 20, fill="black")
    if result == 4:
        create_circle(100, 100, 20, fill="black")
        create_circle(100, 200, 20, fill="black")
        create_circle(200, 100, 20, fill="black")
        create_circle(200, 200, 20, fill="black")
    if result == 5:
        create_circle(100, 100, 20, fill="black")
        create_circle(100, 200, 20, fill="black")
        create_circle(150, 150, 20, fill="black")
        create_circle(200, 100, 20, fill="black")
        create_circle(200, 200, 20, fill="black")
    if result == 6:
        create_circle(100, 100, 20, fill="black")
        create_circle(100, 150, 20, fill="black")
        create_circle(100, 200, 20, fill="black")
        create_circle(200, 100, 20, fill="black")
        create_circle(200, 150, 20, fill="black")
        create_circle(200, 200, 20, fill="black")

button_roll = tk.Button(root, text="کلیک کن", command=roll_dice)
button_roll.pack()

root.mainloop()