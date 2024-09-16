# Text based low or high
import random

title="""
        █░░ █▀▀█ █░░░█   █▀▀█ █▀▀█   █░░█ ░▀░ █▀▀▀ █░░█
        █░░ █░░█ █▄█▄█   █░░█ █▄▄▀   █▀▀█ ▀█▀ █░▀█ █▀▀█
        ▀▀▀ ▀▀▀▀ ░▀░▀░   ▀▀▀▀ ▀░▀▀   ▀░░▀ ▀▀▀ ▀▀▀▀ ▀░░▀                                  
"""

match_game = 5

def game():
    score = 0
    match = 0
    print(title)

    print("you're win if you forcast atleast 3 of 5 games.")
    print("")
    print("You can select low or high as below,")
    print("low = 0")
    print("high = 1")
    print("")

    for x in range(match_game):
        print("Round ", x+1)
        input_player = int(input())
        sys_random = random.randint(0, 10)

        print("Point is :", sys_random)
        if (sys_random < 5 and input_player == 0) or (sys_random >= 5 and input_player == 1):
            score += 1
            print("Your forecast is correct !!")
        else: 
            print("Your forecast is incorrect !!")

    print("=============================================")
    print("")
    print("")
    print("Your score is", score)

    print("=============================================")
    if ( score >= 3 ):
        print("You Win !!!")
    else:
        print("You Lose !!!")

game()