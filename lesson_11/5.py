class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.s = self.area()

    def area(self):
        s = self.a * self.b
        return s

rect1 = Rectangle(4, 2)
rect2 = Rectangle(8, 1)
rect3 = Rectangle(16, 2)
print(rect2.s)
print(rect1.s)
print(rect3.s)