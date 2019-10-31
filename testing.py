import random

position = [19]
print(position)
position[0] -= 5
print(position)
position.clear()
position.append(1)
print(position)


def roll():
    return random.randint(1,1000)


def test():
    print("testing testing")
    roll1 = roll()
    print("You rolled", roll1)
    input(">>>")
    test()


test()
