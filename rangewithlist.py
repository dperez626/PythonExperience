numbers = list(range(1, 6))
print(numbers)

#range function with list to find even numbers

even_numbers = list(range(2, 11, 2))
print(even_numbers)

#square numbers
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

#square numbers more concisely
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#examples of minimum, maximum, and sum

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#squares but uses a list comprehension:
squares = [value**2 for value in range (1,11)]
print(squares)