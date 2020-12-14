class Vehicle:
    def vehicle_method(self):
        return "A parent method from Vehicle class"

#Vehicle class inheritance
class Car(Vehicle):
    def car_method(self):
        return "Daughter class method"

car = Car()
print(car.vehicle_method())
print(car.car_method())