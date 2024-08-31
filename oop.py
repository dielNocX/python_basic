import string
# 1. Class Animal
class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

# 2. Class Cat (inherits from Animal)
class Cat(Animal):
    def deskripsi(self):
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"

    def suara(self):
        return "meow!"

# 3. Instance of Cat class
myCat = Cat("Neko", 3, "Persian")
# ----------------------------------------------------------------------
# Test the instance
print(myCat.deskripsi())  # Output: Neko adalah kucing berjenis Persian yang sudah berumur 3 tahun
print(myCat.suara())  # Output: meow!





# 1. Class Animal
class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

# 2. Class Cat (inherits from Animal)
class Cat(Animal):
    def deskripsi(self):
        return self.name +" adalah kucing berjenis " +self.species+ " yang sudah berumur " + str(self.age) + " tahun"

    def suara(self):
        return "meow!"

# 3. Instance of Cat class
myCat = Cat("Neko", 3, "Persian")

# Test the instance
print(myCat.deskripsi())  # Output: Neko adalah kucing berjenis Persian yang sudah berumur 3 tahun
print(myCat.suara())  # Output: meow!



