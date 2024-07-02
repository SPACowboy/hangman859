import random

# Step 1: Create a list of your favorite fruits
fruits_list = ["Mango", "Strawberry", "Blueberry", "Orange", "Apple"]

# Step 2: Print a random fruit from the list
random_fruit = random.choice(fruits_list)
print("Random fruit:", random_fruit)

# Step 3: User Input and Validation
guess = input("Guess a letter in the random fruit's name (or enter 'q' to quit): ")

if len(guess) == 1 and guess.isalpha():
    # Valid input (single letter and alphabetical)
    print("Good guess!")
else:
    # Invalid input (not a single letter or not alphabetical)
    print("Oops! That is not a valid input. Please enter a single letter.")

# Optional display of entered letter
# print("You entered:", guess)

# Print the randomly chosen word
word = random.choice(fruits_list)
print("The random fruit was:", word)

