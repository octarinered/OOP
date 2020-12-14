class Car:
    #Class variable
    car_count = 0
    
    #Constructor
    def __init__(self, mark, year, price):
        self.mark = mark      # public variable
        self._year = year     # protected variable (uses one "_")
        self.__price = price  # private variable (uses two "_" = "__")

    #Special str method is uses to initialize class description
    #If you dont use it and try to print class object it will print place in memory
    # where object is located  
    def __str__(self):
        return "Car class Object"

    #Simple method
    def output(self):
        Car.car_count += 1
        return "{} {} {} {}".format(self.mark, self._year, self.__price, Car.car_count)

    #Obviously static method
    @staticmethod
    def class_details():
        return "This is a Car class"

    #Method with local variable - a variable that can't be called elswhere in code
    def start(self):
        message = "Engine is running"
        return message

#How objects are initializing
car1 = Car("Mark1", 1999, 200000)
car2 = Car("Mark22", 2002, 44000)

print(car1.output())
print(car2.start())

print(Car.class_details())
