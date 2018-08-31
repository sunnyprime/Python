# class circle():
#
#     pi = 3.14
#
#     def __init__(self,radius=1):
#         self.radius = radius
#
# myc = circle()
# print(myc.radius)
# ==================================

class circle():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius * circle.pi

    def set_radius(self,new_r):
        self.radius = new_r

myc = circle(30)
# myc.radius = 100
myc.set_radius(999)
print("area",myc.area())
# print(myc.radius)
