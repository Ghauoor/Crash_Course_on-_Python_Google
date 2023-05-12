def format_address(address_string):
    house_number = ""
    street_name = ""

    # Separate the house number from the street name.
    address_parts = address_string.split()

    for address_part in address_parts:
        # Check if the address part is numeric or not
        if address_part.isnumeric():
            house_number = address_part
        else:
            street_name += address_part + " "

    # Remove the extra space at the end of the last "street_name".
    street_name = street_name.strip()

    # Use string formatting to return the required formatted string.
    return "House number {} on a street named {}".format(house_number, street_name)


print(format_address("123 Main Street"))


def highlight_word(sentence, word):
    # Replace all occurrences of the word with its upper-case version
    highlighted = sentence.replace(word, word.upper())
    return highlighted


print(highlight_word("Have a nice day", "nice"))
# Should print: "Have a NICE day"


def alphabetize_lists(list1, list2):
    new_list = []  # Initialize a new list.
    new_list = list1 + list2  # Combine the lists.
    new_list.sort()  # Sort the combined lists.
    return new_list


Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]

print(alphabetize_lists(Aniyahs_list, Imanis_list))


def squares(start, end):
    return [n**2 for n in range(start, end + 1)]


print(squares(2, 3))


def car_listing(car_prices):
    result = ""
    for car, price in car_prices.items():
        result += f"A {car} costs {price} dollars\n"
    return result


print(
    car_listing(
        {
            "Kia Soul": 19000,
            "Lamborghini Diablo": 55000,
            "Ford Fiesta": 13000,
            "Toyota Prius": 24000,
        }
    )
)

guest_list = {
    "Adam": 3,
    "Camila": 3,
    "David": 5,
    "Jamal": 3,
    "Charley": 2,
    "Titus": 1,
    "Raj": 6,
    "Noemi": 1,
    "Sakira": 3,
    "Chidi": 5,
}


def check_guests(guest_list, guest):
    return guest_list[guest]


print(check_guests(guest_list, "Adam"))


def count_letters(text):
    # Initialize a new dictionary.
    dictionary = {}
    # Complete the for loop to iterate through each "text" character and
    # use a string method to ensure all letters are lowercase.
    for char in text.lower():
        # Complete the if-statement using a string method to check if the
        # character is a letter.
        if char.isalpha():
            # Complete the if-statement using a logical operator to check if
            # the letter is not already in the dictionary.
            if char not in dictionary:
                # Use a dictionary operation to add the letter as a key
                # and set the initial count value to zero.
                dictionary[char] = 0
            # Use a dictionary operation to increment the letter count value
            # for the existing key.
            dictionary[char] += 1
    return dictionary


print(count_letters("AaBbCc"))
