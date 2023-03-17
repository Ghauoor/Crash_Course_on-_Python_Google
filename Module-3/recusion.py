def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


print(factorial(4))


def sum_positive_numbers(n):
    if n < 1:
        return n

    return n + sum_positive_numbers(n - 1)


print(sum_positive_numbers(5))


def fibonachi_series(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonachi_series(n - 1) + fibonachi_series(n - 2)


print(fibonachi_series(5))


def is_power_of(number, base):
    if number < base:
        return number == 1

    return is_power_of(number // base, base)


print(is_power_of(8, 2))


def sequence(low, high):
    for x in range(2):
        for y in range(high, low - 1, -1):
            if y == low:
                print(str(y))
            else:
                print(str(y), end=", ")


sequence(1, 3)
