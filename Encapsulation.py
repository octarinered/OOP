class Car:

    #Constructor
    def __init__(self, model):
        self.model = model

    #Model property
    @property
    def model(self):
        return self.__model

    #Model setter for poperty (kinda data filter)
    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2018:
            self.__model = 2018
        else:
            self.__model = model

    def getCarModel(self):
        return "Model release year" + str(self.model)

carA = Car(2008)
print(carA.getCarModel())