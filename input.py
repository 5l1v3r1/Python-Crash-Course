#7-1. Rental Car:

rental_car = input("What kind of rental car would you like?")
print("Let me see if I can find you a " + rental_car.title() + ".")

#7-2. Restaurant Seating:

people = int(input("\nHow many people are in your dinner group?"))
if people >= 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready!")

#7-3. Multiples of Ten:
ask_user = int(input("\nEnter a number: "))
if ask_user % 10 == 0:
    print("The number's a mulitple of 10.")
else:
    print("The number's not a multiple of 10.")
