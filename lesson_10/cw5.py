class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coord(self, a):
        if a == "x":
            return self.x
        elif a == "y":
            return self.y

    def dist(self, p2):
        # self = point_1, p2 = point_2
        d = ((self.x - p2.x)**2 + (self.y - p2.y)**2)**0.5
        return d


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

point_1 = Point(x1, y1)
point_2 = Point(x2, y2)

print(point_1.dist(point_2))


