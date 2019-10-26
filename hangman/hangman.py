import time
import random

name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")

time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

secret_words = ["banana", "guitar", "python", "hacktober", "github", "rice"]
secret_word = random.choice(secret_words)
guesses = ''
turns = len(secret_word)

while turns > 0:         
    dashes_left = 0             

    for char in secret_word:      
        if char in guesses:    
            print(char, end = "")
        else:
            print("_", end = "")
            dashes_left += 1    
    if dashes_left == 0:        
        print("\nYou won!")
        break              

    print()

    guess = input("guess a character:")
    if guess and guess[0]:
        guesses += guess[0]

    if guess and guess[0] not in secret_word:  
        turns -= 1        
        print("Wrong\n")    
        print("You have", + turns, 'more guesses')

        if turns == 0:           
            print("You lost.")
            print("The correct word is:", secret_word)
