import tkinter as tk
import random

def guess_word(): # function to pick out a random word from the .txt file
    with open("words.txt", "r", encoding="utf-8") as file:
        word = [line.strip() for line in file.readlines()]
        word_num = random.randint(0,len(word)-1)
        chosen_word = word[word_num]
        return chosen_word

def new_masked_word(a, b, c): # function to unmask the word
    updated_masked_word = list(b)
    for i in range(len(a)):
        if a[i] == c:
            updated_masked_word[i] = c
    return "".join(updated_masked_word)

def hangman(): # main function
    correct_word = guess_word()
    inc_letters = []
    inc_guesses = 0
    loss = 11
    masked_word = ("_" * len(correct_word))
    guessed_word = ""
    print("guess the word!")
    
    while guessed_word != correct_word:
        print(masked_word)
        user_input = str(input(":"))

        if not user_input.isalpha(): # 3 if/elif statements to check for invalid inputs
            print("[Invalid Input]")
            print("Please try letters within the swedish alphabet")
        elif user_input in inc_letters or user_input in masked_word:
            print("[Invalid Input]")
            print("You've already tried that letter")
        elif len(user_input) != 1:
            print("[Invalid Input]")
            print("Please guess with single letters")

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



"""
plan 
done:
 take random word from file
 make a seperate string the same length to compare
 ask users input - input one letter
 iterate through word from file
 if correct reveal letter - variable with value on the crypted word
 if crypted word has specifik value the word has been guessed
 if incorrect add to a variable
 if the variable crosses threshold its lose
 keep repeating until win or lose

in progress:
add option to guess either letter or word
ui stuff
 """