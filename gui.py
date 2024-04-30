import tkinter as tk
import random

chosen_word = ""

def guess_word():
    global chosen_word

    with open("words.txt", "r", encoding="utf-8") as file:
        word = [line.strip() for line in file.readlines()]
        word_num = random.randint(0,len(word)-1)
        chosen_word = word[word_num]

    print(chosen_word)
    
root = tk.Tk()
root.title("hangman")
root.geometry("700x500")

title = tk.Label(root, text="Welcome, input a letter or word!")
title.pack()

first_input = tk.Entry(root)
first_input.pack()

def get_input():
    guess = first_input.get()
    return guess

inc_letters = []
inc_guesses = 0

def inc_guess(a):
    loss = 11
    global inc_letters
    global inc_guesses

    inc_letters.append(a)
    inc_guesses += 1
    print(inc_letters)
    print(inc_guesses)

    if inc_guesses == loss:
        print("you lost")

def new_masked_word(correct, b, a):
    updated_masked_word = list(a)
    for i in range(len(correct)):
        if correct[i] == b:
            updated_masked_word[i] = b
    masked_word = "".join(updated_masked_word)   

def button_command(correct):
    user_input = get_input().lower()

    print(f"{masked_word} masked_word")

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
            
            print(masked_word)

        else:
            inc_guess(user_input)

            print(inc_guesses)
    print(inc_letters)

guess_button = tk.Button(
    root,
    text="guess",
    command=lambda: button_command(chosen_word)
)
 
guess_button.pack()

next_button = tk.Button(
    root,
    text="next",
    command=guess_word
    
)

next_button.pack()

root.mainloop()