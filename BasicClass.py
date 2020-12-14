class Car:
    
    def __init__(self, mark, year, price):
        self.mark = mark
        self.year = year
        self.price = price

    def output(self):
        return "{} {} {}".format(self.mark, self.year, self.price)

car1 = Car("Mark1", 1999, 200000)
car2 = Car("Mark22", 2002, 44000)

print(car1.output())
print(car2.output())
