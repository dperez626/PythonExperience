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