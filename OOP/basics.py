class Apple:
    color = ""
    flavor = ""


# New Instance
jonaGold = Apple()
jonaGold.color = "Red"
jonaGold.flavor = "Sweet"

print(jonaGold.color)
print(jonaGold.flavor)


class Sparrow:
    name = "Sparrow"
    year = 0

    def speak(self):
        print("Oink! i'm {}! Onink".format(self.name))

    def spparow_years(self):
        return self.year * 19


hamlet = Sparrow()
hamlet.name = "Hamlet"
hamlet.speak()

# Second instances
chicho = Sparrow()
chicho.name = "chicho"
chicho.speak()


class Dog:
    years = 0

    def dog_years(self):
        return self.years * 7


fido = Dog()
fido.years = 3
print(fido.dog_years())
