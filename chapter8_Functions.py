
#Defining a function
#greeter.py
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

#Passing Information to a function
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

#8-1 Message
def display_message():
    print("Hi everyone, I'm learning all about Functions with Python in chapter 8! I'm excited to see what I'll learn!")

display_message()

#8-2 Favorite Book
def favorite_book(title):
    print(f"One of my favorite books is {title.title()}")

favorite_book("Alice in wonderland")

# Passing Arguments
# Positional Arguments
# pets.py
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

# Multiple Function Calls
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'coheed')
describe_pet('dog', 'cambria')

#Order Matters in Positional Arguments