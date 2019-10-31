# Group Members:
# 30 October 2019
# Here we're playing a board game.
# Candy Land

from random import *
position = [1]
# Landing on 13 sends you back 2 steps, landing on a 19 sends you back to tile 1


def play():
    play1 = input(">>>").title()
    if play1 == "Yes" or play1 == "Y":
        print("Alright, lettuce get this show on the road!")
    elif play1 == "No" or play1 == "N":
        print("Lml, noob!XD")
        exit()
    else:
        print("Yes or No answers please.")
        play()


def roll_dice():
    return randint(1, 8)


def rules():
    print("""\t1. You will roll a dice to move about the board.
    2. You must get to spot 20 to win. If your position is equal to 0, you lose!
    3. If you roll a 1 or 3, you move back 1 step.
    4. If you roll a 5, you move back 2 steps.
    5. If you roll a 2 or 4, you move forward 1 step.
    6. If you roll a 6 or 8, you move forward 2 steps.
    7. If you roll a lucky 7, you get to roll again.""")


def candy_land():
    while position[0] <= 0:
        print("Game over!")
        print("You Lost!")
        print("Would you like to play again?")
        again = input(">>>").title()
        if again == "Yes" or again == "Y":
            print("Coolio.")
            position.clear()
            position.append(1)
            input("Press Enter")
            candy_land()
        else:
            print("How is your body feeling? I bet it's sore!")
            print("Sore loser!")
            exit()

    while position[0] == 13:
        print("You landed on 13")
        print("You have been moved back 2 spaces")
        position[0] -= 2
        input("Press Enter")
        candy_land()

    while position[0] == 19:
        print("LML, you couldn't have been more unlucky")
        print("No way did you just land on 19")
        position.clear()
        position.append(1)
        print("You've just been moved to position 1...")
        print("You have to start all over")
        input("Press Enter")
        candy_land()

    roll = roll_dice()
    print(f"You rolled a {roll_dice()}")
    if roll == 1 or roll == 3:
        print("You have been moved back one space.")
        position[0] -= 1  # What this does is subtract from the list value itself so when you want to add you would put +=
        input("Press Enter to continue")
        candy_land()

    # You that if statement as a guide to write the other elif
    # The if statements will call the function and the function will continue to check the position value each time
    # Hit me up if anything


print("Hello user, what is your name?")
name = input(">>>").title()
print(f"Ahh, nice to meet you {name}.")
print("My name is...")  # Make up a name M.
print("Would you like to play a game? *Yes or No*")
play()
print(f"""This game is called Candy Land.
Let me explain the rules to you, {name}.""")
rules()
input("Press Enter when you wish to move on")
candy_land()
