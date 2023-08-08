#cars.py
cars= ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#toppings.py
requested_toppings = 'mushrooms'
if requested_toppings != 'anchovies':
    print('Hold the anchovies!')

#magic_numbers.py
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

#toppings.py testing the in Keyword(if value is in list.
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
'pepperoni' in requested_toppings

#banned_users.py
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

#5-1 Conditional Tests
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\n Is car == 'audi'? I predict False.")
print(car == 'audi')

anime = 'one piece'
tv = 'the bear'
if tv not in anime:
    print(f"{tv.title()}, is not an anime, but instead a tv show!")
print("Is anime == 'one piece'? I predict True.")
print(anime == 'one piece')
print(f" \n Is 'The Bear' == anime? I predict False. ")
print(anime == 'the bear')

food = 'hamburger'
print("\nIs food == 'hamburger'? I predict True.")
print(food == 'hamburger')
print("Is food == 'Pizza', I predict False.")
print(food == 'pizza')

dinner_guest = ['paul']
print("\n Is Paul a dinner guest? I predict True")
print(dinner_guest == ['paul'])
print("Is dinner_guest == 'john', I predict false.")
print(dinner_guest == ['john'])

#5-2 More conditional testing(techniically all ifs after the first one is suppose to be elif but for sake of this code thier all if.
favorite_animal = 'tiger'
if favorite_animal == 'tiger':
    print(f"\n{favorite_animal.title()} is your favorite animal")
if favorite_animal != 'tiger':
    print(f"{favorite_animal.upper()}, is not your favorite animal.")
if favorite_animal == 'duck':
    print(f"\n Duck is your favorite animal")
if favorite_animal != 'duck':
    print(f"Duck is not your favorite animal, but a {favorite_animal} is!")

fruit = 'BANANA'
if 'BANANA' not in fruit:
    print(f"\n{fruit.lower()} is not a fruit!")
elif 'BANANA' in fruit:
    print(f"\n{fruit.lower()} is a fruit!")

drinking_age = 21
age_1 = 19
age_2 = 25
age_3 = 23
age_4 = 21
age_5 = 20
if age_1 < drinking_age:
    print("\nYour to young to drink.")
elif age_1 >= drinking_age:
    print("You can have a drink.")
if age_2 < drinking_age:
    print("Your to young to drink.")
elif age_2 >= drinking_age:
    print("You can have a drink.")
if age_3 < drinking_age:
    print("Your to young to drink.")
elif age_3 >= drinking_age:
    print("You can have a drink.")
if age_4 < drinking_age:
    print("Your to young to drink.")
elif age_4 >= drinking_age:
    print("You can have a drink.")
if age_5 < drinking_age:
    print("Your to young to drink.")
elif age_5 >= drinking_age:
    print("You can have a drink.")

if age_3 and age_2 >= drinking_age:
    print("\nWe can go out for drinks!")
elif age_3 and age_2 <= drinking_age:
    print("We can not get drinks!")

if age_1 and age_5 <= drinking_age:
    print("\nWe can not get drinks!")
elif age_1 and age_5 >= drinking_age:
    print("We can go out for drinks!")

if age_1 or age_4 <= drinking_age:
    print("Only one of you can drink!")

colors = ['black', 'red', 'purple', 'silver', 'pink']
if 'blue' in colors:
    print("\nBlue is in colors list!")
elif 'blue' not in colors:
    print("\nBlue is not in colors list!")

if 'black' in colors:
    print("Black is in colors list!")
elif 'black' not in colors:
    print("Black is not in colors list!")

#voting.py
age = 19
if age >= 18:
    print("\nYou are old enough to vote!")
    print("Have you registered to vote yet?")
age = 17
if age >= 18:
    print("\nYou are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("\nSorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#amusement_park.py if-elif-else Chain
age = 12

if age < 4:
    print("\nYour admission cost is $0.")
elif age < 18:
    print("\nYour admission cost is $25.")
else:
    print("\nYour admission cost is $40.")

#consice amusement_park.py if-elif-else chain
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"\nYour admission cost is ${price}.")

#amusement_park.py Using multiple elif Blocks
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"\nYour admission cost is ${price}.")

#amusement_park.py Omitting the else Block
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"\nYour admission cost is ${price}.")

#toppings.py
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding Mushrooms')
if 'pepperoni' in requested_toppings:
    print('Adding Pepperoni')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print('\nFinished making your pizza!')

# 5-3 Alien Colors #1
alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color:
    print('\nYou just earned 5 points!')

if 'black' in alien_color:
    print('\nYou earned no points, Black is not an alien color.')

#5-4 Alien Colors #2.1
alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color:
    points = 5
if not 'green' in alien_color:
    points = 10
print(f'\nYou won a total of {points}!')

#5-4 Alien Colors #2.2
alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color:
    points = 5
else:
    points = 10

print(f'\nCongrats! You won a total of {points}!')

#5-5 Alien Colors #3
alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color:
    print('\nYou earned 5 points')
if 'yellow' in alien_color:
    print('You earned 10 points')
if 'red' in alien_color:
    print('You earned 15 points')

#5-6 Stages of Life
age = 31

if age < 2:
    print('\nYou are a baby!')
elif age <= 4:
    print('\nYou are a toddler!')
elif age <= 13:
    print('\nYou are a kid!')
elif age <= 20:
    print('\nYou are a teenager!')
elif age < 65:
    print('\nYou are an adult!')
elif age >= 65:
    print('\nYour are an elder person!')

#5-7 Favorite Fruit
favorite_fruit = ['pineapple', 'coconut', 'passion fruit']

if 'pineapple' in favorite_fruit:
    print('\nYou really like Pineapples!')
if 'coconut' in favorite_fruit:
    print('\nYou really like Coconuts!')
if 'passion fruit' in favorite_fruit:
    print('\nYou really like Passion fruits!')
if 'banana' in favorite_fruit:
    print('\nYou really like bananas')
if 'mango' in favorite_fruit:
    print('\nYou really like mangos!')

#toppings.py
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f'\nAdding {requested_topping}')
print('\nFinished making your pizza!')

#toppings.py if pizzeria ran out of green peppers
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('\nSorry, we are out of green peppers right now.')
    else:
        print(f'\nAdding {requested_topping}.')
print('\nFinished making your pizza!')

#toppings.py checking if list is empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}.')
    print('\nFinished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')
#toppings.py using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}.')
    else:
        print(f'Sorry, we dont have {requested_topping}.')
print('\nFinished making your pizza!')

#my own practice
available_guitars = ['fender', 'gibson', 'dean', 'ltd']
requested_guitars = ['fender', 'gibson', 'micheal kelly', 'dean']

for requested_guitar in requested_guitars:
    if requested_guitar in available_guitars:
        print(f'\nAdding {requested_guitar} to the order!')
    else:
        print(f'Sorry we dont carry {requested_guitar} here.')

print('\n Your order is complete!')

#5-8 Hello Admin
usernames = ['Connor', 'Victor', 'admin', 'Jesse', 'Samantha']

for username in usernames:
    if username == 'admin':
        print(f'Hello Admin, would you like a status report?')
    else:
        print(f'\nHello {username}, thank you for logging in.')
#if statement below works if all names in usernamers is removed
if usernames == []:
    print('We need some users!')

#5-9 Hello Admin No users printing empty list
usernames = []

for username in usernames:
    if username == 'admin':
        print(f'Hello Admin, would you like a status report?')
    else:
        print(f'\nHello {username}, thank you for logging in.')
if usernames == []:
    print('\nWe need some users!')

#5-10 Hello Admin.py checking Usernames
current_users = ['ltd5layer', 'deanM@achine', 'Fendurr', 'Gibsun', 'ROSE']
new_users = ['ROSE', 'Kramernutz', 'Costa', 'Fendurr', 'Odin', 'rose']

for new_user in new_users:
    if new_user in current_users:
        print(f"I'm sorry but {new_user} is already taken!")
    else:
        print(f"{new_user} is available!")

#5-11 Oridinal Numbers:
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for number in numbers:
    if number == '1':
        print(f'{number}st')
    elif number == '2':
        print(f'{number}nd')
    elif number == '3':
        print(f'{number}rd')
    else:
        print(f'{number}th')