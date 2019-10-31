# Group Members:
# 30 October 2019
# Here we're playing a board game.
# Candy Land

from random import *

location = ["Lose", "Spot1", "", "", "", "", "", "", "", "", "", "", "", "13", "", "", "", "", "", "19", "Win"]
# Landing on 13 sends you back 2 steps, landing on a 19 sends you back to tile 1


def roll_dice():
    return randint(1, 8)


def rules():
    print("""1. You will roll a dice to move about the board.
    2. You must get to spot 20 to win. If you land on 0, you lose!
    3. If you roll a 1 or 3, you move back 1 step.
    4. If you roll a 5, you move back 2 steps.
    5. If you roll a 2 or 4, you move forward 1 step.
    6. If you roll a 6 or 8, you move forward 2 steps.
    7. If you roll a lucky 7, you get to roll again.""")


def candy_land():
    roll_dice()
    print(f"You rolled a {roll_dice()}")

    if roll_dice() == 1 or 3:






def play():
    play1 = input(">>>").title()
    if play1 == "Yes" or "Y":
        print("Alright, lettuce get this show on the road!")
    elif play1 == "No" or "N":
        print("Lml, noob! Too bad for you! XD")
        exit()
    else:
        print("Yes or No answers please.")
        play()


print("Hello user, what is your name?")
name = input(">>>").title()
print(f"Ahh, nice to meet you {name}.")
print("My name is...")  # Make up a name M.
print("Would you like gto play a game? *Yes or No*")
play()
print(f"""This game is called Candy Land.
Let me explain the rules to you, {name}.
""")  # I'll let you explain the rules
candy_land()
