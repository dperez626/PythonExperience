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

#Returning a simple value
#formatted_name.py
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#Making an Argument Optional
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

#middle name optional
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#Returning a Dictionary
#person.py
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

#greeter.py with a break
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#This is not an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

def build_person(first_name, last_name, age=None):
    """Return a dictionary """
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)


#greeter.py with a break
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#This is not an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

#8-6 City Names
def city_country(city, county):
    both = f"{city.title()}, {county.title()}"
    return both

location = city_country('belgrade', 'Serbia')
print(location)
location = city_country('bogota', 'colombia')
print(location)
location = city_country('Hamburg', 'germany')
print(location)

#8-7 Album
def make_album(artist_name, album_title):
    album = {'Artist': artist_name.title(), 'Title': album_title.title()}
    return album

music = make_album('mastodon', 'hushed and grim')
print(music)
music = make_album('bad bunny', 'un verano sin ti')
print(music)
music = make_album('2 cellos', 'let there be cello')
print(music)

#8-7 pt.2 Album
def make_album(artist_name, album_title, number_songs = None):
    album = {'Artist': artist_name.title(), 'Title': album_title.title()}
    if number_songs:
        album['Number of Songs'] = number_songs
    return album

music = make_album('mastodon', 'hushed and grim')
print(music)
music = make_album('bad bunny', 'un verano sin ti')
print(music)
music = make_album('2 cellos', 'let there be cello')
print(music)
music = make_album("coheed & cambria", "good apollo I'm burning star IV volume one: from fear through the eyes of madness", 15)
print(music)

#8-8 User Albums
def make_album(artist_name, album_title):
    album = {'Artist': artist_name.title(), 'Title': album_title.title()}
    return album

while True:
    print("\nPlease enter a album:")
    print("(Enter q at anytime to quit.)")

    album_artist = input("Artist Name: ")
    if album_artist == 'q':
        break
    album_name = input("Album Title: ")
    if album_name == 'q':
        break

    formatted_album = make_album(album_artist, album_name)
    print(formatted_album)

music = make_album('mastodon', 'hushed and grim')
print(music)
music = make_album('bad bunny', 'un verano sin ti')
print(music)
music = make_album('2 cellos', 'let there be cello')
print(music)

#greet_users.py
def greet_users(names):
    """Print a simpler greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#printing_models.py
#Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

#Organized greet_user.py
def print_models(unprinted_designs, completed_models):
    """ Simulate printing eacg design, until """