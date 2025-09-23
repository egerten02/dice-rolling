import random
import tkinter as tk
from tkinter import PhotoImage

window = tk.Tk()
window.title("Dice Rolling")
window.focus_force()

faces = ["one.png", "two.png", "three.png", "four.png", "five.png", "six.png"]

dice = PhotoImage(file="./images/roll.png")
display = tk.Label(window, image=dice)

def roll(event=None):
    dice_image = PhotoImage(file=f"./images/{random.choice(faces)}")
    display.configure(image=dice_image)
    display.PhotoImage = dice_image

display.bind("<Button-1>", roll)
display.pack()
window.mainloop()