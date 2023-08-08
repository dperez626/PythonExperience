#dimensions.py
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#will get an error, can not change values of tuples.
#dimensions[0] = 250

#looping through LL VALUES IN A TUPLE
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

#writing over a tuple
dimensions = (200, 50)
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)
