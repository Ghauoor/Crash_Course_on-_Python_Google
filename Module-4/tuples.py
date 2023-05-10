fullName = ("Ghayoor", "Hussain")

# Oder matter in tuples


def conver_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


# When a func return more then one val it return a tuple
result = conver_seconds(5000)
print(type(result))

# unpack the tuple
hours, minutes, seconds = result

print(hours, minutes, seconds)


# itrate over tuple

animals = ["Lion", "Monke", "Dolphin"]

chars = 0

for animal in animals:
    chars += len(animal)
print("total character {}, Average len: {}".format(chars, chars / len(animals)))

winner = ["Ghayoor", "Foo", "Bar"]
for index, person in enumerate(winner):
    print("{} - {}".format(index + 1, person))


def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))

    return result


print(
    full_emails(
        [("ghayoor@example.com", "ghayoor"), ("hussain@example.com", "hussain")]
    )
)
