class Vehicle:
    def print_details(self):
        return "Parent method from Vehicle class"

class Car(Vehicle):
    #Parent method overloading
    def print_details(self):
        return "Daughter method from Car class"

class Cycle(Vehicle):
    #Parent method overloading
    def print_details(self):
        return "Daughter method from Cycle class"

car1 = Vehicle()
car2 = Car()
car3 = Cycle()

print(car1.print_details())
print(car2.print_details())
print(car3.print_details())