import tkinter as tk
import random

chosen_word = ""
inc_letters = []
inc_guesses = 0
words_list = []
inc_words = 0
masked_word = ""
score = 0

root = tk.Tk()
root.title("hangman")
root.geometry("700x500")

speech_bubble = tk.Label(root, wraplength="200")
first_input = tk.Entry(root)
masked = tk.Label(root)
gletter_title = tk.Label(root, text="Incorrect Letters:")
guessed_letters = tk.Label(root)
gword_title = tk.Label(root, text="Incorrect Words:")
guessed_words = tk.Label(root, wraplength="200")
iimage = tk.PhotoImage(file="h0.ppm").subsample(3, 3)
dimage = tk.Label(root, image=iimage)
score_count = tk.Label(root, text=f"score: {score}")

def guess_word():
    global chosen_word
    global masked_word

    global inc_letters
    global inc_guesses
    global words_list

    inc_letters = []
    inc_guesses = 0
    words_list = []

    with open("words.txt", "r", encoding="utf-8") as file:
        word = [line.strip() for line in file.readlines()]
        word_num = random.randint(0,len(word)-1)
        chosen_word = word[word_num]

    masked_word = ("_ "*len(chosen_word))
    print(chosen_word)

    guessed_letters.config(text=inc_letters)
    guessed_words.config(text=words_list)

    masked.config(text=masked_word)
    next_button.place(relx=0.95, rely=0.05, anchor="center")    
    guess_button.place(relx=0.2, rely=0.5, anchor="center")
    speech_bubble.config(text="Input a letter or word!")
    first_input.delete(0, tk.END)
    update_image(inc_guesses)

def update_image(ig):
    image_list = ["h0", "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10"]
    new_image = tk.PhotoImage(file=image_list[ig]+".ppm").subsample(3, 3)
    dimage.config(image=new_image)
    dimage.image = new_image

def get_input():
    guess = first_input.get()
    return guess

def inc_guess(i, l):
    global inc_guesses

    loss = 10
    l.append(i)
    inc_guesses += 1
    update_image(inc_guesses)

    if inc_guesses == loss:
        speech_bubble.config(text=f"You lost! The correct word was {chosen_word}")
        next_game()
    
    guessed_letters.config(text=l)

def inc_word(i, w):
    global inc_words

    loss = 2
    w.append(i)
    inc_words += 1
    if inc_words == loss:
        speech_bubble.config(text=f"You lost! The correct word was {chosen_word}")
        next_game()
    guessed_words.config(text=w)
    
def next_game():
    guess_button.place_forget()
    first_input.delete(0, tk.END)
    next_button.place(relx=0.5, rely=0.7, anchor="center")

def new_masked_word(correct, b, mask):
    global masked_word
    
    updated_masked_word = list(mask)
    for i in range(len(correct)):
        if correct[i] == b:
            updated_masked_word[i] = b
    masked_word = "".join(updated_masked_word)

    if masked_word == chosen_word:
        print("[Condition] - Win")
        speech_bubble.config(text="You won")
        next_game()

    # display
    masked.config(text=masked_word)

def button_command(correct):
    global score

    user_input = get_input().lower()

    if not user_input.isalpha():
        print("[Invalid Input] - not recognized letter")
    elif user_input in inc_letters or user_input in masked_word:
        print("[Invalid Input] - repeated letter")
    elif len(user_input) != 1:

        if user_input == correct:                                         #winning conditions
            speech_bubble.config(text="You got it correct!")
            masked.config(text=correct)
            next_game()
            score += 1
            score_count.config(text=f"Score: {score}")

        else:
            inc_word(user_input, words_list)

    else:
        if user_input in correct:
            new_masked_word(correct, user_input, masked_word)
        else:
            inc_guess(user_input, inc_letters)

        first_input.delete(0, tk.END)
    
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

    gletter_title.place(relx=0.8, rely=0.65, anchor="center")
    guessed_letters.place(relx=0.8, rely=0.68, anchor="center")

    gword_title.place(relx=0.8, rely=0.85, anchor="center")
    guessed_words.place(relx=0.8, rely=0.88, anchor="center")   

    next_button.place(relx=0.95, rely=0.05, anchor="center")
    
    first_input.place(relx=0.2, rely=0.4, anchor="center")
    guess_button.place(relx=0.2, rely=0.5, anchor="center")

    score_count.place(relx=0.05, rely=0.05, anchor="center")
    dimage.place(relx=0.5, rely=0.4, anchor="center")

    start_button.destroy()

    guess_word()

start_button = tk.Button(root, text="Start", command=start_game)
start_button.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()