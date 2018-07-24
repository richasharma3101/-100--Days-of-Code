# Imports
import random

print("\t\tWelcome to our Word Guess Game...")
print("\t\t\n Instructions:")
print("\nYou have only 5 attempts to guess the word")

WORDS = ("Java", "Cobol", "Python", "Javascript", "Instructions")
word = random.choice(WORDS)
correct = word
tries = 1
hint = word[0]

# Tell the player the length of the word and let them guess it for the first time
print("Length of the word: ", len(word),"\n")
guess = input("Guess the word: ")

while guess.lower() != correct.lower() and guess != "" and tries <= 5:
    print("No!")
    tries += 1
    if tries == 3:
        response = input("Would you like a hint? y or n: ")
        if response.lower() == "y":
            print("The first letter of the word is: ", hint)
    print("\nTries remaining: ", 6-tries)
    guess = input("Guess the word: ")
    
# Tell the player they was right or ran out of tries
if guess.lower() == correct.lower():
    print("\nYes! You guessed the word! The word was: ", correct)
    print("You guessed it in ", tries)
else:
    print("\nNo! You ran out of tries!")
    
input("\n\nThank You.")
