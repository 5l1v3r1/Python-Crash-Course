import random

ask_user = input("Do you want to roll a pair of dice?")

if ask_user == "yes":
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(dice1)
    print(dice2)
    if dice1 == 1 and dice2 == 1:
        print("SNAKE EYES!")
        ask_user = input("Do you want to roll again?")
        if ask_user == "yes":
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            print(dice1)
            print(dice2)
            if dice1 == 1 and dice2 == 1:
                print("SNAKE EYES!")
            else:
                print("Have a great day!")
    else:
        print("Have a great day!")
elif ask_user == "no":
    print("Bye!")

else:
    print("Bye!")