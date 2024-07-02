import random
# Step 1: Create a list of your 5 favorite fruits
fruits_list = ["Mango", "Strawberry", "Blueberry", "Orange", "Apple"]

# Step 2: Assign the list to a variable called word_list
word_list = fruits_list

# Step 3: Print out the list
print("My 5 favorite fruits:", word_list)

random_fruit = random.choice(fruits_list)
print("Random fruit:", random_fruit)

word = random.choice(fruits_list)

# Step 3: Print the randomly chosen word
print("Random fruit:", word)


guess = input("Enter a single letter: ")

# (Optional) Display the entered letter (can be added after Step 2)
print("You entered:", guess)
