import math

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        a = math.pi*self.radius**2
        return a
    
    def perimeter(self):
        p = 2*math.pi*self.radius
        return p

c1 = circle(3)
print("Area of circle: ", c1.area())
print("Perimeter of circle: ", c1.perimeter())