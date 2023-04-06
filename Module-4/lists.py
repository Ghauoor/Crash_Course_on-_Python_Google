x = ["Now", "I", "am", "cooking"]
print(type(x))

print(x)

print("I" in x)

print(x[1:3])

# first value is default to zero
print(x[:2])
# second value is len of list
print(x[2:])

# Mutability of Lists
fruits = ["Apple", "Bannana", "Melon"]

fruits.append("Kiwi")
print(fruits)
fruits.insert(0, "Peach")

fruits.remove("Melon")

fruits.pop(3)

fruits[2] = "Strawberry"

print(fruits)

