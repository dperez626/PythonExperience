#parrot.py
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#greeter.py
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

#greeter.py part 2
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

#rollercoaster.py
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

#even_or_add.py
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")


#7-1 Rental Car
car = input("What kind of car would you like? ")
print(f"Let me see if i can find you a {car}!")

#7-2 Resturant Seating
number = input("How many people are in your group tonight? ")
number = int(number)

if number > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready")

#7-3 Multiples of Ten
number = input("Pick any number: ")
number = int(number)

if number % 10 == 0:
    print("This number is a multiple of 10.")
else:
    print("This number is not a multiple of 10.")

#counting.py
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


#parrot.py
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
message = " "
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)


prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

#cities.py
prompt = "\nPlease enter the name of the city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go {city.title()}!")


#counting.py
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)


#counting.py
x = 1
while x <= 5:
    print(x)
    x += 1


#7-4 Pizza Toppings
prompt = "\nWhat kind of toppings do you like on your pizza? "
prompt += "\n(Enter 'quit' when you are finished.) "
message = " "
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(f"I'll add {message} to your pizza.")




#7-5 Movie Tickets
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print(" You are free!")
    elif age < 13:
        print(" Your ticket is $10.")
    else:
        print(" Your ticket is $15.")



# Moving items from one list to another
# confirmed_users.py

# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


#Removing all instances of Specific Values from a list
#pets.py
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


# Filling a Dictionary with User Input
# mountain_poll.py
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")



# 7-8 Deli
sandwich_orders = ['cuban', 'chimi', 'BLT', 'Tuna', 'chopped cheese']
finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()

    print(f"I made your {finished_sandwich.title()} sandwich. Please enjoy!")
    finished_sandwiches.append(finished_sandwich)

print(f"\nTo confirm these are the sandwiches you ordered: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())


# 7-9  No Pastrami
sandwich_orders = ['pastrami', 'cuban', 'pastrami', 'chimi', 'pastrami', 'BLT', 'Tuna', 'chopped cheese']
finished_sandwiches = []
print("We are out of Pastrami sandwiches!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()

    print(f"I made your {finished_sandwich.title()} sandwich. Please enjoy!")
    finished_sandwiches.append(finished_sandwich)

print(f"\nTo confirm these are the sandwiches you ordered: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())


#7-10 Dream Vacation
locations = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    location = input("If you could visit one place in the world, where would you go? ")

    locations[name] = location

    repeat = input ("Is there anyone else to respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n*** Results ***")
for name, location in locations.items():
    print(f"{name.title()}'s dream vacation is in {location.title()}.")