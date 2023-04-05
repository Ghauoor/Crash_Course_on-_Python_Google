name = "Ghayoor"
color = "gold"
print(name[1])


text = "Random String with alot of chars"
print(text[-1])

# slice
color[1:4]


pets = "Cats & Dogs"
print(pets.index("&"))

print("Cat" in pets)


# replace old domain with new domain
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain

        return new_email
    return email


# more string methods

"Ghayoor".upper()
"Ghayoor".lower()

" Ghayoor ".strip()
" Ghayoor ".lstrip()
" Ghayoor ".rstrip()

"this is a String".count("a")

"Naruto".endswith("a")
"Naruto".isnumeric()
" ".join(["this", "is", "a", "phrase", "joined", "by", "spaces"])

"This is another String".strip()


# Formate the String

name = "Ghayoor"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))


def student_grade(name, grade):
    return "{} received {}% on the exam".format(name, grade)


price = 7.5
with_tax = price * 1.09

print(price, with_tax)

# Formate the price
print("Base price is: {:.2f} with Tax : {:.2f}".format(price, with_tax))


def replace_ending(sentence, old, new):
    if sentence.endswith(old):
        i = len(sentence) - len(old)
        new_sentence = sentence[:i] + new
        return new_sentence

    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
