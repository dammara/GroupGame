# Group Members:
# 30 October 2019
# Here we're playing a board game.
# Candy Land

from random import *

location = ["Lose", "", "", "", "", "", "", "", "", "", "", "", "", "13", "", "", "", "", "", "19", "Win"]
# Landing on 13 sends you back 2 steps, landing on a 19 sends you back to tile 1


def dice():
    roll_dice = randint(1, 8)
    print(roll_dice)


def candy_land():
    print("")


def rules():
    print("""1. You will roll a dice to move about the board.
    2. You must get to spot 20 to win. If you land on 0, you lose!
    3. If you roll a 1 or 3, you move back 1 step.
    4. If you roll a 5, you move back 2 steps.
    5. If you roll a 2 or 4, you move forward 1 step.
    6. If you roll a 6 or 8, you move forward 2 steps.
    7. If you roll a lucky 7, you get to roll again.""")


def play():
    play1 = input(">>>").title()
    if play1 == "Yes" or "Y" or "y" or "yes":
        print("Alright, lettuce get this show on the road!")
    elif play1 == "No" or "N" or "no" or "n":
        print("Lml, noob! Too bad for you! XD")
        exit()
    else:
        print("Yes or No answers please.")
        play()


# Splash Screen
print("Hello user, what is your name?")
name = input(">>>").title()
print(f"Ahh, nice to meet you {name}.")
print("My name is...")  # Make up a name M.
print("Would you like to play a game? *Yes or No*")
play()
print(f"""This game is called Candy Land.
""")
print("Let me explain the rules to you, {name}.")
rules()
candy_land()

