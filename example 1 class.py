class Car():
    def __init__(self, make, model):
        self.make = "make"
        self.model= "model"

vehicle1 = Car("toyota", "carmy")
vehicle1.make = "toyota"
vehicle1.model = "camry"


class Electric_car(Car):
    def __init__(self, battery_size):
        self.make= "make"
        self.model = "model"
        self.battery_size= "size"

vehicle2 = Car("Tesla", "S")
vehicle2.make = "Tesla"
vehicle2.model = "S"
vehicle2.size = "110kWh"

print(vehicle2.size)