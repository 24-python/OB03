class Shape():
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

#Написать функцию, которая принимает объект класса Shape и выводит его площадь.

def area(shape):
    print(f"Площадь: {shape.area()}")


circle = Circle(5)
rectangle = Rectangle(5, 10)
square = Square(5)

area(circle)
area(rectangle)
area(square)
