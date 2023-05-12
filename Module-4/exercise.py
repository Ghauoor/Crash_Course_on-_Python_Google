# Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

newfilenames = [
    name.replace(".hpp", ".h") if name.endswith(".hpp") else name for name in filenames
]

print(newfilenames)


# Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.
def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    for word in words:
        # Check if the first letter is a vowel
        if word[0] in "aeiouAEIOU":
            # If it is, add "ay" to the end of the word
            say += word + "ay" + " "
        else:
            # If it isn't, move the consonant cluster to the end of the word, and add "ay"
            consonant_cluster = ""
            i = 0
            while i < len(word) and word[i] not in "aeiouAEIOU":
                consonant_cluster += word[i]
                i += 1
            say += word[i:] + consonant_cluster + "ay" + " "
    # Remove the last space and return the translated text
    return say[:-1]


# The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.
def group_list(group, users):
    members = ", ".join(users)
    return "{}: {}".format(group, members)


print(
    group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])
)  # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(
    group_list("Engineering", ["Kim", "Jay", "Tom"])
)  # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", ""))  # Should be "Users:"


# The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that.
def guest_list(guests):
    for guest in guests:
        name, age, occupation = guest
        print("{} is {} years old and works as {}".format(name, age, occupation))


guest_list([("Ken", 30, "Chef"), ("Pat", 35, "Lawyer"), ("Amanda", 25, "Engineer")])


# Dictionary


def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append(user + "@" + domain)
    return emails


print(
    email_list(
        {
            "gmail.com": ["clark.kent", "diana.prince", "peter.parker"],
            "yahoo.com": ["barbara.gordon", "jean.grey"],
            "hotmail.com": ["bruce.wayne"],
        }
    )
)


def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            # Now add the group to the the list of
            # groups for this user, creating the entry
            # in the dictionary if necessary
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)
    return user_groups


print(
    groups_per_user(
        {
            "local": ["admin", "userA"],
            "public": ["admin", "userB"],
            "administrator": ["admin"],
        }
    )
)

wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
new_items = {"jeans": ["white"], "scarf": ["yellow"], "socks": ["black", "brown"]}
print(wardrobe.update(new_items))


def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for item, price in basket.items():
        # Add each price to the total calculation
        total += price
    # Limit the return value to 2 decimal places
    return round(total, 2)


groceries = {
    "bananas": 1.56,
    "apples": 2.50,
    "oranges": 0.99,
    "bread": 4.59,
    "coffee": 6.99,
    "milk": 3.39,
    "eggs": 2.98,
    "cheese": 5.44,
}

print(add_prices(groceries))


