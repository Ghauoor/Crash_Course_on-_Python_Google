class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)


jonaGold = Apple("red", "sweet")
print(jonaGold)


class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return "hi, my name is {}".format(self.name)


some_person = Person("Ghayoor")
print(some_person.greeting())
