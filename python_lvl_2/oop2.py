# class Dog():

    # def __init__(self,breed):
    #     self.breed = breed

# mydog = Dog(breed = "Lab")
# otherdog = Dog(breed="Huskie")
# print(mydog.breed)
# print(otherdog.breed)
# ===========================================
# class Dog():
#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name = name
#
# mydog  = Dog("Lab","Sammy")
# print(mydog.breed)
# print(mydog.name)
# ============================================
class Dog():

    #CLASS OBJECT ATTRIBUTE
    species = "mammal"

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

mydog  = Dog("Lab","Sammy")
print(mydog.breed)
print(mydog.name)
print(mydog.species)
