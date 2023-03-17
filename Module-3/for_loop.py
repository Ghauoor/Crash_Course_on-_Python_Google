for x in range(5):
    print(x)


product = 1

for n in range(1, 10):
    product *= n

print(product)


def to_celcius(x):
    return (x - 32) * 5 / 9


for item in range(0, 101, 10):
    print(item, to_celcius(item))

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


for x in "banana":
    print(x)


for x in range(2, 30, 3):
    print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break


for x in range(2, 6):
    print(x)


for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()

for n in range(0, 101, 7):
    if n != 0:
        print(n)
    else:
        print(0)
