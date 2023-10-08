class vehicle:
    def vehicle_info(self):
        print("inside vehicle class")
class car(vehicle):
    def carinfo(self):
        print("inside car class")
car=car()
car.vehicle_info()
car.car_info()