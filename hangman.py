import tkinter as tk
import random

g_word = open("words.txt", "r", encoding='utf-8') as file:


#plan 
# take random word from file
# make a seperate string the same length to compare
# ask users input - input one letter
# iterate through word from file
# if correct reveal letter - variable with value on the crypted word
# if crypted word has specifik value the word has been guessed
# if incorrect add to a variable
# if the variable crosses threshold its lose
# keep repeating until win or lose
# add option to guess either letter or word
# ui stuff