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

# Example usage (assuming you have a word list named 'words')
# game = Hangman(words)  # Assuming 'words' is a list of words
