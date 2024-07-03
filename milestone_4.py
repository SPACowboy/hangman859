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
        Checks if the guessed letter is in the hidden word and updates word_guessed if correct.

        Args:
            guess (str): The letter guessed by the player.

        Returns:
            bool: True if the guess is in the word, False otherwise.
        """

        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")

            # Update word_guessed with the correct guess
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess

            # Reduce num_letters only if the guess revealed a new letter (not a duplicate)
            if guess not in self.list_of_guesses:
                self.num_letters -= 1

            return True  # Indicate a correct guess
        else:
            return False  # Indicate an incorrect guess

# ... rest of your code (e.g., ask_for_input)


# We'll create the ask_for_input method in the next step

def ask_for_input(self):
        """
        Prompts the user for a guess and validates it.
        """

        while True:
            guess = input("Guess a letter: ")

            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                # Valid guess, check if it's in the word and update list_of_guesses
                is_correct_guess = self.check_guess(guess)
                self.list_of_guesses.append(guess)

                # Potential additional logic based on guess result (e.g., update word_guessed)
                return is_correct_guess
