# Step 1: Infinite loop for continuous gameplay
hidden_word = "salama"
guessed_letters = []  # List to store guessed letters (initially empty)
remaining_guesses = 6  # Example: Set a number of allowed wrong guesses

def check_guess(guess):
    """
    Checks if the guessed letter is in the hidden word.

    Args:
        guess (str): The letter guessed by the user.

    Returns:
        bool: True if the guess is in the hidden word, False otherwise.
    """

    guess = guess.lower()
    return guess in hidden_word

def ask_for_input():
    """
    Prompts the user for a guess and validates the input.

    Returns:
        str: The user's valid guess (single letter or 'q' to quit).
    """

    while True:
        guess = input("Guess a letter in the hidden word (or 'q' to quit): ")

        if guess.isalpha() or guess == 'q':
            if guess == 'q':
                print("Thanks for playing!")
                exit()
            else:
                return guess
        else:
            print("Invalid letter. Please enter a single alphabetical character (or 'q' to quit).")

# Main loop with game logic
while True:
    guess = ask_for_input()  # Call the function to get user input
    is_correct_guess = check_guess(guess)  # Call the function to check the guess

    # Update guessed letters
    guessed_letters.append(guess)

    if is_correct_guess:
        print("Good guess!")
        # Reveal the guessed letter in the hidden word display (implementation depends on your choice)
    else:
        print("Sorry, that's incorrect.")
        remaining_guesses -= 1  # Decrement remaining guesses

    # Check win/lose conditions
    if all(letter in guessed_letters for letter in hidden_word):  # Check if all letters in hidden_word are in guessed_letters
        print("Congratulations! You guessed the word.")
        break  # Exit the loop if player wins
    elif remaining_guesses == 0:
        print("Sorry, you ran out of guesses. The word was:", hidden_word)
        break  # Exit the loop if player loses

    # Display remaining guesses (optional)
    # print("Remaining guesses:", remaining_guesses)
