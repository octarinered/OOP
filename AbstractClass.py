#In the core of the python language, abstract classes are not represented, 
# the first ones were implemented in the standard abc module

from abc import ABC, abstractmethod, abstractproperty

class Movable(ABC):

    @abstractmethod
    def move(self):
        return "Move"

    @abstractproperty
    def speed(self):
        pass


class Car(Movable):
    speed = 200
    def move(self):
        return "Car move method"

car = Car()
print(car.move())










