#alien.py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

#alien.py accessing values in a dictionary
alien_0 = {'color': 'green'}
print(alien_0['color'])

#alien.py accessing both values in the dictionary
alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print(f"\nYou just earned {new_points} points!")

#alien.py adding new key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#alien.py starting with an empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

#alien.py modifying values in a dictionary
alien_0 = {'color': 'green'}
print(f"\nThe alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"\nThe alien is now {alien_0['color']}.")

#alien.py modifying values in a dictionary part 2
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"\nOriginal position: {alien_0['x_position']}")

#Move the alien to the right
#Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

#The new position is the old postion plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")


#Removing Key-Value Pairs
alien_0 = {'color': 'green' , 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)#be aware that the deleted key-value pair is removed permanetly.


#Dicitionary of Similar Objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
language = favorite_languages['sarah'].title()
print(f"\nSarah's favorite langauge is {language}.")

#Using get() to Access Values
#alien_no_points.py
alien_0 = {'color': 'green', 'speed': 'slow'}
#print(alien_0['points'])

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

#Try it yourself
#6-1 Person
person = {'first name': 'Leida', 'last name': 'Torres', 'age': 30, 'city': 'NY'}
print(person['first name'])
print(person['last name'])
print(person['age'])
print(person['city'])
print(person.values())

#6-2 Favorite numbers
favorite_number = {
    'Me': 69,
    'Jae': 13,
    'Leida': 15,
    'Susan': 45,
    'Beth': 22,
    }
print(favorite_number)
print(favorite_number.items())

#6-3 Glossary
glossary = {
    'stoic': 'describes someone who shows very little emotion especially in response to a painful or distressing situation.',
    'null': 'having no value',
    'evince': 'formal word that means "to display clearly" Someone who evinces an attitude, emotion, quality, wtc., shows it clearly.',
    'illustrious': 'describes a person or deed that is highly admired and respected.',
    'ameliorate': 'is a formal word that means "to make something, such as a problem, better or more tolerable."'
    }
print(f"\nStoic -\n{glossary['stoic']}\n")
print(f"Null -\n{glossary['null']}\n")
print(f"Evince -\n{glossary['evince']}\n")
print(f"Illustrious -\n{glossary['illustrious']}\n")
print(f"Ameliorate -\n{glossary['ameliorate']}")

#user.py
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")


#favorite_languages.py
favorite_languages ={
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}.")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(f"\n{name.title()}, thank you for taking the poll.")


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

#6-4 Glossary
glossary = {
    'stoic': 'describes someone who shows very little emotion especially in response to a painful or distressing situation.',
    'null': 'having no value',
    'evince': 'formal word that means "to display clearly" Someone who evinces an attitude, emotion, quality, wtc., shows it clearly.',
    'illustrious': 'describes a person or deed that is highly admired and respected.',
    'ameliorate': 'is a formal word that means "to make something, such as a problem, better or more tolerable.',
    'dictionary': 'a collection of key-value pairs that maps together data types. A key can e thought of as a category while the values are the different ways to describe, count or respond to that category. The key is immutable which means it must have a unique name that is different than any other variable name in your code. The values can be any data type, e.g., string, integer, or Boolean. It is often abbreviated as dict.',
    'element': 'one of the values in a list(or other sequence).',
    'for loop': 'A statement in Python that is useful for working through a list of items. The loop repeats a statement over and over until it has iterated through or touched all the possible items.',
    'key': 'A data item that is mapped to a value in a dictionary. Keys are used to look up values in a dictionary.',
    'value': 'A string (series of characters)or an integer (number) that can be stored in a variable.',
    'tuple': 'A data type that contains a sequence of items of any type, like a list, but the contents cannot be changed.',
    'slice': 'a part of a string(substring).',
    'loop': 'A statement or a group of statements that execute repeatedly until a terminating condition is satisfied.',
    'nested loop': 'a loop nested inside the body of another loop.',
    'nested list': 'a list that is an element of another list.'
    }
for key, value in glossary.items():
    print(f"\n{key}: {value}")

#6-5 Rivers
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}
for river, country in rivers.items():
    print(f"\nThe {river.title()} runs though {country.title()}.")

for river in rivers.keys():
    print(f"{river}")
for country in rivers.values():
    print(f"{country}")

#aliens.py
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

#Make an empty list for storing aliens.
aliens = []

#Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'

# Show the first 5 aliens.
for alien in aliens [:5]:
    print(alien)
print("...")

# Store information about pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

#Summerize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

#favorite_languages.py
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

#many_users.py
users = {
    'aeinstein' :{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

#6-7 People
people = {
    'person1': {
        'first name': 'Leida',
        'last name': 'Torres',
        'age': 30,
        'city': 'NY'
    },
    'person2': {
        'first name': 'darrle',
        'last name': 'perez',
        'age': 31,
        'city': 'NY'
    },
    'person3': {
        'first name': 'maru',
        'last name': 'victor',
        'age': 18,
        'city': 'hellsgate'
    }
}

for person, people_info in people.items():
    print(f"Person: {person}")
    full_name = f"{people_info['first name']} {people_info['last name']}"
    age = f"{people_info['age']}"
    location = f"{people_info['city']}"

    print(f"Full name: {full_name.title()}")
    print(f"\t Age: {age}")
    print(f"\t Location: {location}")


#6-8 Pets
pets = {
    'beans': {
        'breed': 'lab',
        'owner': 'josh'
    },
    'rox': {
        'breed': 'husky',
        'owner': 'karen'
    },
    'nimbus': {
        'breed': 'mainecoon',
        'owner': 'cookie'
    },
    'dexter': {
        'breed': 'cockapoo',
        'owner': 'heather'
    },
    'marmaduke': {
        'breed': 'orange tabby',
        'owner': 'max'
    }
}

for pet, pets_info in pets.items():
    print(f"Name: {pet.title()}")
    breed = f"{pets_info['breed']}"
    owner = f"{pets_info['owner']}"

    print(f"\tBreed: {breed.title()}")
    print(f"\tOwner: {owner.title()}")

#6-9 Favorite Places
favorite_places = {
    'zak': ['utah', 'mexico', 'new york'],
    'justin': ['peru', 'atl', 'uk'],
    'erica': ['colombia', 'brazil', 'norway']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")

#6-10 Favorite Number
favorite_numbers = {
    'Me': ['69', '15', '111', '333'],
    'Jae': ['13', '69', '44'],
    'Leida': ['15', '22', '33'],
    'Susan': ['45', '91', '99'],
    'Beth': ['22', '100', '1752020']
}
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are: ")
    for number in numbers:
        print(f"\t{number}")

#6-11 Cities
cities = {
    'tampa': {
        'country': 'US',
        'population': 387050,
        'fact': 'Home of the lightning'
    },
    'oslo': {
        'country': 'norway',
        'population': 634293,
        'fact': 'Founded at the end of the Viking Age in 1040'
    },
    'lima': {
        'country': 'peru',
        'population': '7600000',
        'fact': 'Second largest city built in a desert'
    }
}
for city, city_info in cities.items():
    print(f"City: {city.title()}")
    country = f"{city_info['country']}"
    population = f"{city_info['population']}"
    fact = f"{city_info['fact']}"
    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tFun Fact: {fact}")
