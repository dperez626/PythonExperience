"""#parrot.py
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
"""

#7-4 Pizza Toppings
prompt = "\nWhat kind of toppings do you like on your pizza? "
message = f"I'll add that topping to the pizza! "
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)