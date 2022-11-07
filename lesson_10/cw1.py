class Car: 
    def __init__(self, mark, fuel_type, color, engine_volume, max_speed, probeg, fuel_left, fuel_per_km):
        self.car_mark = mark
        self.fuel_type = fuel_type
        self.color = color
        self.engine_volume = engine_volume
        self.max_speed = max_speed
        self.probeg = probeg
        self.fuel_left = fuel_left
        self.fuel_for_km = fuel_per_km

    def get_attributes(self):
        print(self.car_mark)
        print(self.color)
        print(self.engine_volume)
        print(self.max_speed)
        print(self.probeg)

    def km_left(self):
        s = self.fuel_left / self.fuel_for_km
        return s

    def is_electric_car(self):
        if self.fuel_type == "electricity":
            return True
        else:
            return False


car_1 = Car("mersedes", "electricity", "black", 3.0, 400, 2000, 120, 9.2)
car_2 = Car("bmw", "petrol", "white", 2.0, 500, 100000, 150, 15.56)

print(car_1.km_left())
print(car_2.km_left())
print(car_1.is_electric_car())
print(car_2.is_electric_car())