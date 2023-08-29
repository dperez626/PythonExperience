
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
#Default Values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

#8-3 T-Shirt (Positional argument)
def make_shirt(size, text):
    print(f"\nI have a {size} shirt that says {text} on it!")

make_shirt('large', 'cool breeze')

#8-3 T-Shirt (Keyword Argument)
def make_shirt(size, text):
    print(f"\nI have a {size} shirt that says {text} on it!")

make_shirt(size='large', text='cool mist')

def make_shirt(size, text):
    print(f"\nI have a {size} shirt that says {text} on it!")

make_shirt(text='cool wind', size='large')

#8-4 Large Shirt
def make_shirt(text='I love python', size='large'):
    print(f"\nI have a {size} shirt that says {text} on it!")

make_shirt(text='deep water')

def make_shirt(text='I love python', size='large'):
    print(f"\nI have a {size} shirt that says {text} on it!")

make_shirt(size='small')

#8-5 Cities
def describe_city(city_name, country='Peru'):
    print(f"\n{city_name.title()} is in {country.title()}.")

describe_city('lima')
describe_city('huaraz')
describe_city('ambato', country='ecuador')