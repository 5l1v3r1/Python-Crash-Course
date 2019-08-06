sandwich_orders  = ['cheesesteak', 'sloppy joe', 'french dip', 'banh mi', 'gyro']

finished_sandwiches = []

for sandwich in sandwich_orders:
    print("I made your " + sandwich.title() + "!")
    sandwich_orders.remove(sandwich)
    finished_sandwiches.append(sandwich)
    for finished_sandwich in finished_sandwiches:
        print("*" * 30)
        print(finished_sandwich.title() + " COMPLETED!")
        print("*" * 30)
