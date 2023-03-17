x = 0

while x < 5:
    print("Not there yet, X = " + str(x))
    x = x + 1
print("X= " + str(x))


def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")


attempts(5)


def count_down(start_number):
    current = 3
    while current > 0:
        print(current)
        current -= 1
    print("Zero!")


count_down(3)


def print_range(start, end):
    n = start
    while n <= end:
        print(n)
        n += 1


print_range(1, 5)


def multiplication_table(number):
    multiplier = 1

    while multiplier <= 5:
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1


multiplication_table(3)

multiplication_table(5)

multiplication_table(8)
