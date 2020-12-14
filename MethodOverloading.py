#Python isn't allow method overloading as other languages 
# (Several methods with same name and different parameters)
#Here we use if-else construction
class Car:
    def start(self, a, b=None):
        if b is not None:
            return a + b
        else:
            return a 