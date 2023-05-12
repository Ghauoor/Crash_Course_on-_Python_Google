# Key Value Pair
file_count = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(file_count)

print(file_count["txt"])
print("html" in file_count)

file_count["cfg"] = 8
print(file_count)

# if key is already exist then it will replace old
# key with new key

file_count["cfg"] = 10
print(file_count)

del file_count["txt"]
print(file_count)

# itration over dictionary
for extention in file_count:
    print(extention)

# items method returns tuple in return
# tuple first ele is key and second is it's value

for ext, amount in file_count.items():
    print("There are {} files with .{} extention".format(amount, ext))

print(file_count.keys())
print(file_count.values())

for value in file_count.values():
    print(value)

cool_beasts = {"octopuses": "tentacles", "dolphins": "fins", "rhinos": "horns"}
for beast, feature in cool_beasts.items():
    print("{} have {}".format(beast, feature))


def count_letter(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


print(count_letter("Ghayoor"))


# This function receives a dictionary, which contains resource
# categories (keys) with a list of available resources (values) for a
# company’s IT Department. The resources belong to multiple categories.
# The function should reverse the keys and values to show which
# categories (values) each resource (key) belongs to.
def invert_resource_dict(resource_dictionary):
    # Initialize a "new_dictionary" variable as a dict data type using
    # empty {} curly brackets.
    new_dictionary = {}
    # The outer for loop iterates through each "resource_group" and
    # associated "resources" in the "resource_dictionary" items.
    for resource_group, resources in resource_dictionary.items():
        # The inner for loop iterates over each "resource" value in
        # the list of "resources" for one "resource_group" key at a time.
        for resource in resources:
            # The if-statement checks if the current "resource" value has
            # been appended as a key to the "new_dictionary" yet.
            if resource in new_dictionary:
                # If True, then append the "resource_group" as a value to the
                # "resource", which is now the key.
                new_dictionary[resource].append(resource_group)
            # If False (else), then add the "resource" as a new key with the
            # "resource_group" as a value for that key.
            else:
                new_dictionary[resource] = [resource_group]
    # Return the new dictionary once the outer for loop has completed
    # all iterations.
    return new_dictionary


print(
    invert_resource_dict(
        {
            "Hard Drives": ["IDE HDDs", "SCSI HDDs"],
            "PC Parts": [
                "IDE HDDs",
                "SCSI HDDs",
                "High-end video cards",
                "Basic video cards",
            ],
            "Video Cards": ["High-end video cards", "Basic video cards"],
        }
    )
)
# This function receives a dictionary, which contains common employee
# last names as keys, and a list of employee first names as values.
# The function generates a new list that contains each employees’ full
# name (First_name Last_Name). For example, the key "Garcia" with the
# values ["Maria", "Hugo", "Lucia"] should be converted to a list
# that contains ["Maria Garcia", "Hugo Garcia", "Lucia Garcia"].


def list_full_names(employee_dictionary):
    # Initialize the "full_names" variable as a list data type using
    # empty [] square brackets.
    full_names = []

    # The outer for loop iterates through each "last_name" key and
    # associated "first_name" values, in the "employee_dictionary" items.
    for last_name, first_names in employee_dictionary.items():
        # The inner for loop iterates over each "first_name" value in
        # the list of "first_names" for one "last_name" key at a time.
        for first_name in first_names:
            # Append the new "full_names" list with the "first_name" value
            # concatenated with a space " ", and the key "last_name".
            full_names.append(first_name + " " + last_name)

    # Return the new "full_names" list once the outer for loop has
    # completed all iterations.
    return full_names


print(
    list_full_names(
        {
            "Ali": ["Muhammad", "Amir", "Malik"],
            "Devi": ["Ram", "Amaira"],
            "Chen": ["Feng", "Li"],
        }
    )
)
