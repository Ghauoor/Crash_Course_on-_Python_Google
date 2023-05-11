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


def skip_elements(elements):
    result = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            result.append(element)

    return result


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))


multiple = []

for x in range(1, 11):
    multiple.append(x * 7)


print(multiple)

# same code as above but using list comprehensions
# List comprehensions create a new list based on sequences or range

multiple = [x * 7 for x in range(1, 11)]

languages = ["Python", "Perl", "Kotlin", "Java", "C"]
lengths = [len(language) for language in languages]

print(lengths)

numbers = [x for x in range(0, 101) if x % 3 == 0]


# print(numbers)
def odd_numbers(n):
    return [x for x in range(1, n + 1) if x % 2 != 0]


def squares(start, end):
    return [x * x for x in range(start, end + 1)]

