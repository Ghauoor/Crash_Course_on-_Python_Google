def greeting(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)


greeting("Ghayoor Hussain", "IT Support")


# ? Return statement func
def area_triangle(base, height):
    return base * height / 2


area_a = area_triangle(5, 7)
area_b = area_triangle(7, 3)

sum = area_a + area_b
print("The sum of both areas is " + str(sum))


def convert_second(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remain_sec = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remain_sec


hours, minutes, seconds = convert_second(5000)
print(hours, minutes, seconds)


def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))


lucky_number("Ghayoor")
