class Car: 
    def __init__(self, mark, fuel_type, color, engine_volume, max_speed, probeg, price, is_fixed):
        self.car_mark = mark
        self.fuel_type = fuel_type
        self.color = color
        self.engine_volume = engine_volume
        self.max_speed = max_speed
        self.probeg = probeg
        if is_fixed:
            self.price = price // 2
        else:
            self.price = price



car_1 = Car("mersedes", "electricity", "black", 3.0, 400, 2000, 100000000, False)
print(car_1.car_mark)
print(car_1.fuel_type)
print(car_1.price)

