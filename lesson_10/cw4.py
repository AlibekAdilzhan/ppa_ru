class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def is_square(self):
        # if self.a == self.b:
        #     return True
        # else:
        #     return False
        return self.a == self.b

rect_1 = Rect(3, 4)
print(rect_1.is_square())