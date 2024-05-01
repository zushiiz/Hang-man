from tkinter import *
import tkinter as tk
import random

chosen_word = ""
inc_letters = []
inc_guesses = 0
masked_word = ""
    
root = tk.Tk()
root.title("hangman")
root.geometry("700x500")

speech_bubble = tk.Label(root, text="Welcome, input a letter or word!")
first_input = tk.Entry(root)
masked = tk.Label(root, text="")
guessed_letters = tk.Label(root, text="Incorrect Letters:")

image_path = "h1.png"
image = tk.PhotoImage(file=image_path)


image_label = tk.Label(root, image=image)
image_label.pack()

def guess_word():
    global chosen_word
    global masked_word

    global inc_letters
    global inc_guesses

    inc_letters = []
    inc_guesses = 0

    with open("words.txt", "r", encoding="utf-8") as file:
        word = [line.strip() for line in file.readlines()]
        word_num = random.randint(0,len(word)-1)
        chosen_word = word[word_num]

    masked_word = ("_"*len(chosen_word))
    print(chosen_word)

    #display
    masked.config(text=masked_word)


def get_input():
    guess = first_input.get()
    return guess

def inc_guess(i, l, g):
    loss = 11

    l.append(i)
    g += 1
    print(l)
    print(g)

    if g == loss:
        print("you lost")
    
    #display

    guessed_letters.config(text=f"Incorrect Letters:{l}")


def new_masked_word(correct, b, mask):
    global masked_word
    
    updated_masked_word = list(mask)
    for i in range(len(correct)):
        if correct[i] == b:
            updated_masked_word[i] = b
    masked_word = "".join(updated_masked_word)

    # display
    masked.config(text=masked_word)

def button_command(correct):
    user_input = get_input().lower()

    guessed_word = ""

    if not user_input.isalpha():
        print("[Invalid Input]")
        print("Please try letters within the swedish alphabet")
    elif user_input in inc_letters or user_input in masked_word:
        print("[Invalid Input]")
        print("You've already tried that letter")
    elif len(user_input) != 1:
        guessed_word = user_input
        if guessed_word == correct:
            print("win")
        else:
            print("inc")
            
    else:
        if user_input in correct:
            new_masked_word(correct, user_input, masked_word)
            
        else:
            inc_guess(user_input, inc_letters, inc_guesses)

            print(inc_guesses)
    print(inc_letters)

guess_button = tk.Button(
    root,
    text="guess",
    command=lambda: button_command(chosen_word)
)

next_button = tk.Button(
    root,
    text="next",
    command=guess_word
    
)

def start_game():
    speech_bubble.pack()
    masked.pack()
    guessed_letters.pack()

    next_button.place(relx=0.95, rely=0.05, anchor="center")

    first_input.place(relx=0.2, rely=0.4, anchor="center")
    guess_button.place(relx=0.2, rely=0.5, anchor="center")

    start_button.destroy()

start_button = tk.Button(root, text="Start", command=start_game)
start_button.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()