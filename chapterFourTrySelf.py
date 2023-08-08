#4-3 counting to twenty
"""for value in range(1, 21):
    print(value)

#4-4 One Million
one_million = list(range(1, 1000001))
print(one_million)

#4-5 Summing a million
print(min(one_million))
print(max(one_million))
print(sum(one_million))

#4-6 Odd numbers
odd_numbers = list(range(1,21,2))
for odd_numbers in odd_numbers:
    print(odd_numbers)

#4-7 Threes
threes = list(range(3,31,3))
for threes in threes:
    print(threes)

#4-8 Cubes
cubes = []
for value in list(range(1,11)):
    cubes.append(value**2)
print(cubes)

#4-9 Cube Comprehension:
cubes = [value **2 for value in range(1,11)]
print(cubes)

#4-10 Slices
cars = ['honda', 'lexus', 'toyota', 'mazda', 'ford']
print('The first three items in the list are:')
for car in cars[0:3]:
    print(car.title())

print('Three items from the middle of the list are:')
for car in cars[1:4]:
    print(car.title())

print('The last three items in the list are:')
for car in cars[2:5]:
    print(car.title())

#4-11 My Pizzas, Your Pizzas
pizza = ['white', 'buffalo', 'extra cheese']
friends_pizza = pizza[:]
print(pizza)
print(friends_pizza)
pizza.append('regular')
friends_pizza.append('mexican')
print(pizza)
print(friends_pizza)


print(f'\nMy favorite pizzas are: ')
for pizza in pizza:
    print(pizza)
print("\nMy friend's favorite pizzas are: ")
for friends_pizza in friends_pizza:
    print(friends_pizza)

#4-12 More Loops with Foods.py
my_foods = ['pizza', 'falafel', 'chocolate cake']
friend_foods = my_foods[:]
my_foods.append('burger')
friend_foods.append('tacos')

print("\nThis is my list of favorite foods: ")
for my_foods in my_foods:
    print(my_foods.title())
print("\nThis is a list of my friends favorite foods: ")
for friend_foods in friend_foods:
    print(friend_foods.title())"""

#4-13 Buffet
buffet = ('steak', 'fried chicken', 'pork chop', 'salmon', 'tofu')
for food in buffet:
    print(food.title())

#code is suppose to give error on purpose
#buffet[0] = 'beans'

buffet = ('steak', 'fried chicken', 'pork chop', 'salad', 'quinoa')
for food in buffet:
    print(food.title())
