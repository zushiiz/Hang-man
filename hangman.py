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

def hangman():

    root = tk.Tk()
    root.title("hangman")
    root.geometry("900x700")

    correct_word = guess_word()
    inc_letters = []
    inc_guesses = 0
    loss = 11
    masked_word = ("_" * len(correct_word))
    guessed_word = ""
    test = "guess the word!"

    label = tk.Label(root, text=test, fg="black")
    label.pack()
    
    while guessed_word != correct_word:
        print(masked_word)
        first_input = str(input(":"))
        user_input = first_input.lower()

        if not user_input.isalpha():
            print("[Invalid Input]")
            print("Please try letters within the swedish alphabet")
        elif user_input in inc_letters or user_input in masked_word:
            print("[Invalid Input]")
            print("You've already tried that letter")
        elif len(user_input) != 1:
            guessed_word = user_input
            if guessed_word == correct_word:
                print("win")
                break
            else:
                print("inc")
                inc_guesses += 1

        else:
            if user_input in correct_word:
                masked_word = new_masked_word(correct_word, masked_word, user_input)
            else:
                inc_letters.append(user_input)
                inc_guesses += 1
                if inc_guesses == loss:
                    print("Sorry you lost")
                    print(f"the correct word was {correct_word}")
                    hangman()
                print(inc_guesses)
        print(inc_letters)

hangman()
