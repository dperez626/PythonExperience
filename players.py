players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

#Looping through a SLICE
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#Copying a List/foods.py
my_foods = ['pizza', 'falafel', 'chocolate cake']
friend_foods = my_foods[:]
my_foods.append('burger')
friend_foods.append('tacos')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#What happens when you try to copy a list without a slice
my_foods = ['pizza', 'falafel', 'chocolate cake']

#this doesn't work:
friend_foods = my_foods

my_foods.append('burger')
friend_foods.append('tacos')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

