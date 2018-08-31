#INHERITANCE
class Animal():

    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("Eating")

class Dog(Animal):

    def __init__(self):
        # Animal.__init__(self)
        print("Dog Created")

    def bark(self):
        print("WOOF")

    def eat(self):
        print("DOG EATING")


# mya = Animal()
# mya.whoAmI()
# mya.eat()

mydog = Dog()
mydog.whoAmI()
mydog.bark()
mydog.eat()
