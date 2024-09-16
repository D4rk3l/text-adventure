# Let's start TRUTH or DARE
# Future plan is to build a web based or an app based game
# Currently runs on the command line

# Welcome the users
print("WELCOME! to truth and dare")

# Number of people
n = int(input("How many people are playing the game?"))

# Write down names for each user
names = []
for i in range(n):
    names.append(input("Name of {0}'th player: ".format(i)))

# Start the game
from numpy import random

# List of truths and dares
# I'll scrape more truths and dares from some website
# Till then play with the below truths and dares
#from questions import truths, dares
truths = ["Do you have a crush on your cousin?", "What's the most weirdest thing you've done on your date?", "Is there anything about your life you would change?", "What's your biggest turn-on?"]
dares = ["Remove your shirt and scream out loudly", "Bark like a dog to a dog"]

while True:
    randomindex = random.randint(0,n)
    randomname = names[randomindex]
    t_or_d = int(input("Truth(1) or Dare(0): "))
    if t_or_d==1:
        answer = input(truths[random.randint(0, len(truths))]+": ")
    elif t_or_d==0:
        answer = input(dares[random.randint(0, len(dares))]+": ")
    else:
        break

print("Thank you for playing :)")
