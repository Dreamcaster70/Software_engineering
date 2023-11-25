class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
circle = Circle(radius=3)
rectangle = Rectangle(width=2, height=4)

shapes = [circle, rectangle]

for shape in shapes:
    print(f"Площадь фигуры: {shape.area()}")