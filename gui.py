import tkinter as tk
import random

def guess_word():
    with open("words.txt", "r", encoding="utf-8") as file:
        word = [line.strip() for line in file.readlines()]
        word_num = random.randint(0,len(word)-1)
        chosen_word = word[word_num]
        return chosen_word
def new_masked_word(a, b, c):
    updated_masked_word = list(b)
    for i in range(len(a)):
        if a[i] == c:
            updated_masked_word[i] = c
    return "".join(updated_masked_word)
def hangman(first_input):
    print("hello world")
   

root = tk.Tk()
root.title("hangman")
root.geometry("900x700")

title = tk.Label(root, text="Welcome, input a letter or word!")
title.pack()

first_input = tk.Entry(root)
first_input.pack()

def get_input():
    guess = first_input.get()
    return guess

first_input = get_input

button = tk.Button(
    root,
    text="guess",
    command=get_input, hangman
)

button.pack()

root.mainloop()