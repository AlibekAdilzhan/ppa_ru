class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coord(self, a):
        if a == "x":
            return self.x
        elif a == "y":
            return self.y


point_1 = Point(5, 10)
a = input() # x

while a != "x" and a != "y":
    print("your input is not correct, please enter x or y")
    a = input()
s = point_1.get_coord(a)
print(s)
