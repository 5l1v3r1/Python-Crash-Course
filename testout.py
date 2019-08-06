import random

dice1 = random.randint(1,6)

dice2 = random.randint(1,6)

if dice1 == 1 & dice2 == 1:
    print("SNAKE EYES!")
else:
    print('-'*15)
    print("First die: " + str(dice1) + "\n" + "Second die: " + str(dice2))
    print('-'*15)