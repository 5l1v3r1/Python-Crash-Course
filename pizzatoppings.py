# 7-4. Pizza Toppings:
prompt = "\nEnter your pizza toppings!"
prompt += "\n(Enter 'quit' to exit the program!)"

the_chef_is_cooking = True

while the_chef_is_cooking:
    toppings = input(prompt)
    if toppings == "quit":
        the_chef_is_cooking = False
    else:
        print("I\'ll add the " + toppings + "!")

# 7.5 Movie Tickets:
person = input("Hello, what is your age?")
person = int(person)

if person < 3:
    print("Your ticket is free!")
elif person >= 3 and person < 12:
    print("Your ticket is $10!")
else:
    print("Your ticket is $15!")