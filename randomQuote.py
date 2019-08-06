pretty = "*"

while True:
    ask_user = input("\nHow are you feeling today?")
    if ask_user == "happy":
        print(pretty * 50)
        print("There is only one happiness in this life, to love and be loved. - George Sands")
        print(pretty * 50)
    elif ask_user == "scared":
        print(pretty * 50)
        print("The real man smiles in trouble, gathers strength from distress, and grows brave by reflection. - Thomas Paine")
        print(pretty * 50)
    elif ask_user == "mad":
        print(pretty * 50)
        print("We are all born mad. Some remain so. - Samuel Beckett")
        print(pretty * 50)
    elif ask_user == "vengeful":
        print(pretty * 50)
        print("The best revenge is to be unlike him who performed the injury. - Marcus Aurelius")
        print(pretty * 50)
    elif ask_user =="surprised":
        print(pretty * 50)
        print("Times changes everything except something within us which is always surprised by change. - Thomas Hardy")
        print(pretty * 50)
    else:
        print(pretty * 50)
        print("Have a nice day!")
        print(pretty * 50)