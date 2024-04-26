import tkinter as tk
import random

root = tk.Tk()
root.title("hangman")
root.geometry("400x100")

title = tk.Label(root, text="Welcome, input a letter or word!")
title.pack()

first_input = tk.Entry(root)
first_input.pack()

def get_input():
    guess = first_input.get()
    return guess

user_input = get_input()

button = tk.Button(
    root,
    text="guess",
    command=get_input
)

button.pack()

print(user_input)

root.mainloop()