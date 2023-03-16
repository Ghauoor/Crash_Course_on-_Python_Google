print(10 > 1)

print("cat" == "dog")

print(1 != 2)

print(1 == "1")

#!_____________________Logical Oprators__________________________
# and --> both expresion will be true or false
print("Ghayoor" > "Hussain" and "Taimoor" > "Hussain")

# or --> either one of them is true
print(25 > 50 or 1 < 2)

# not --> invert the origanl value
print(not 42 == "Answer")

# True or True returns True
print((15 / 3 < 2 + 4) or (0 >= 6 - 7))
True

print((6 * 3 >= 18) and (9 + 9 <= 36 / 2))

print("Nairobi" < "Milan" and "Nairobi" > "Hanoi")

# True or True returns True
print((15 / 3 < 2 + 4) or (0 >= 6 - 7))


#!____________________String Camperision___________________________
# The == operator can check if two strings are equal to each other.
# If they are equal, the Python interpreter returns a True result.
print("a string" == "a string")

# In this example, the equality == comparison is between "4 + 5" and
# 4 + 5. Since the left data type is a string and the right data type
# is an integer, the two values cannot be equal. So, the comparison
# returns a False result.
print("4 + 5" == 4 + 5)

# The != operator can check if the two strings are NOT equal to each
# other. If they are indeed not equal, then Python returns a True result.
print("rabbit" != "frog")


# In this example, the variable event_city has been assigned the string
# value "Shanghai". This variable is compared to a static string,
# "Shanghai", using the != operator. As, the strings "Shanghai" and
# "Shanghai" are the same, the comparison of "Shanghai" != "Shanghai"
# is false. Accordingly, Python will return a False result.
event_city = "Shanghai"
print(event_city != "Shanghai")

# This last example illustrates the result of trying to compare two
# items of different data types using the equality == operator. The
# two items are not equal, so the comparison returns False.
print("three" == 3)


# The greater than > operator checks if the left string has a higher
# Unicode value than the right string. If true, the Python interpreter
# returns a True result. Since W has a Unicode value of 87, and you can
# easily calculate that F has a Unicode value of 70, this comparison is
# the same as 87 > 70. As this is true, Python will return a True
# result.
print("Wednesday" > "Friday")


# The less than < operator checks if the left string has a lower
# Unicode value than the right string. If you reference the Unicode
# chart above, you can see that all lowercase letters have higher
# Unicode values than uppercase letters. We can see that B has a
# Unicode value of 66 and b has a Unicode value of 98. This
# comparison is the same as 66 < 98, which is true. So, Python will
# return a True result.
print("Brown" < "brown")


# If the strings have the same first few letters, the comparison will
# cycle through each letter of each string, from left to right until it
# finds two letters that have different Unicode values. In this example,
# both strings share the initial substring "sun", but then have
# different letters with different Unicode values in the fourth place
# in each string. So, the fourth letters 'b' and 't' of the two
# strings are used for the comparison. Since 'b' does not have a higher
# Unicode value than 't', the comparison returns a False result.
print("sunbathe" > "suntan")


# If two identical strings are compared using the less than < comparison
# operator, this will produce a False result because they are equal.
print("Lima" < "Lima")


# This last example illustrates the result of trying to compare two
# items of different data types using the less than < operator. The
# greater than > and less than operators < cannot be used to compare
# two different data types.
print("Five" < str(6))


#!_____________________________Some Tasks___________________________


def hint_username(username):
    if len(username) < 3:
        print("Invalid Username. Must be atleast 3 charcters")
    elif len(username) > 15:
        print("Invalid Username. Must be under 15 charcters")
    else:
        print("Valid Username")


hint_username("Ghayoor Hussain")


def is_even(number):
    if number % 2 == 0:
        return True
    return False


print(is_even(2))
