# Group Members:
# 30 October 2019
# Here we're playing a board game.
# Candy Land

from random import *
location = []


def dice():
    roll_dice = randint(1, 8)
    print(roll_dice)


def candy_land():
    print()


def play():
    play1 = input(">>>").title()
    if play1 == "Yes" or "Y":
        print("Alright, lettuce get this show on the road!")
    elif play1 == "No" or "N":
        print("Lml, noob! Too bad for you! XD")
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
""")
candy_land()
