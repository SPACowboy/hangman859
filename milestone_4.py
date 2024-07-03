import random

class Hangman:
    """
    This class represents the Hangman game logic.
    """

    def __init__(self, word_list, num_lives=5):
        """
        Initializes the attributes of the Hangman class.

        Args:
            word_list (list): A list of words to choose from.
            num_lives (int, optional): The number of lives the player starts with. Defaults to 5.
        """

        self.word = random.choice(word_list)  # Choose a random word from the list
        self.word_guessed = ['_' for _ in self.word]  # List with underscores for unguessed letters

        # Count unique letters (excluding duplicates)
        self.num_letters = len(set(self.word))

        self.num_lives = num_lives
        self.word_list = word_list  # Store the word list for reference
        self.list_of_guesses = []  # Empty list to store guessed letters

def check_guess(self, guess):
        """
        Checks if the guessed letter is in the hidden word.

        Args:
            guess (str): The letter guessed by the player.

        Returns:
            bool: True if the guess is in the word, False otherwise.
        """

        # Convert guess to lowercase for case-insensitive matching
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            return True  # Indicate a correct guess
        else:
            return False  # Indicate an incorrect guess

# We'll create the ask_for_input method in the next step
