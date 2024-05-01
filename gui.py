import tkinter as tk
import random

chosen_word = ""
inc_letters = []
inc_guesses = 0
masked_word = ""
score = 0

root = tk.Tk()
root.title("hangman")
root.geometry("700x500")

speech_bubble = tk.Label(root)
first_input = tk.Entry(root)
masked = tk.Label(root, text="")
guessed_letters = tk.Label(root, text="Incorrect Letters:")
score_count = tk.Label(root, text=f"score:{score}")

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
    next_button.place(relx=0.95, rely=0.05, anchor="center")    
    guess_button.place(relx=0.2, rely=0.5, anchor="center")
    speech_bubble.config(text="Input a letter or word!")


def get_input():
    guess = first_input.get()
    return guess

def inc_guess(i, l):
    global inc_guesses

    loss = 3
    l.append(i)
    inc_guesses += 1
    if inc_guesses == loss:
        speech_bubble.config(text="You lost")
        next_game()
    
    #display
    guessed_letters.config(text=l)



def next_game():
    guess_button.place_forget()
    next_button.place(relx=0.5, rely=0.5, anchor="center")

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
    global score

    user_input = get_input().lower()

    guessed_word = ""

    if not user_input.isalpha():
        print("[Invalid Input] - not recognized letter")
    elif user_input in inc_letters or user_input in masked_word:
        print("[Invalid Input] - repeated letter")
    elif len(user_input) != 1:
        guessed_word = user_input
        if guessed_word == correct:                                         #winning conditions
            speech_bubble.config(text="You got it correct!")
            masked.config(text=correct)
            next_game()

        else:
            
            print("inc")
            
    else:
        if user_input in correct:
            new_masked_word(correct, user_input, masked_word)
            
        else:
            inc_guess(user_input, inc_letters)

    print(inc_letters)
    print(inc_guesses)

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

    score_count.place(relx=0.05, rely=0.05, anchor="center")

    start_button.destroy()

    guess_word()

start_button = tk.Button(root, text="Start", command=start_game)
start_button.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()