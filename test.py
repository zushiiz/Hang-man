def update_masked_word(word, masked_word, letter):
    """
    Update the masked_word based on the user's guessed letter.
    Replace underscores in masked_word with the guessed letter if it appears in the word.
    """
    updated_masked_word = list(masked_word)  # Convert masked_word to a list to modify it
    
    # Iterate over each character in the word and corresponding position in masked_word
    for i in range(len(word)):
        if word[i] == letter:
            updated_masked_word[i] = letter  # Replace underscore with the guessed letter
    
    return "".join(updated_masked_word)  # Convert the list back to a string


# Example usage:
word_to_guess = "Hello"
masked_word = "_____"

print("Welcome to the word guessing game!")
print(f"Guess the word: {masked_word}")

# Game loop
while masked_word != word_to_guess:
    guess = input("Enter a letter: ").strip().lower()  # Get user's letter guess
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical letter.")
        continue  # Skip the rest of the loop and ask for another guess
    
    # Update the masked_word based on the user's guess
    masked_word = update_masked_word(word_to_guess, masked_word, guess)
    
    # Display the updated masked_word
    print(f"Current progress: {masked_word}")

print("Congratulations! You guessed the word correctly.")