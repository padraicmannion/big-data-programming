# define a class for a car
# implement car object
# init is a name used for when the fields need to be made private (naming convention)
# although in python it's not really possible to have a truly private function, class
# etc because it's not Pythonic.  The class Car inherits from the object base class.
# A car has the variables colour, make, mileage and engineSize for the car base class.
# By using a single or double _ before the variable name defines it as private.
# Private protects the variables from change and means anyone can implement them using
# getters and setters without changing the base object.

class Car(object):
    def __init__(self):
        self.__colour = ' '
        self.__make = ' '
        self.__mileage = 0
        self.engineSize = ' '

        # Getter and setter functions can be implemented in new and different ways and add new
        # functions, variables or functionality etc.  The paint job updates the colour of the specific
        # car object without changing the value held in the private variable.  The move is used to test
        # the car for example 15km's that should make the mileage of the car in turn increase by 15.
        # While get functions only need 1 variable self, all set functions need 2 variables self and
        # the value that is being changed from the default value.

    def getColour(self):
        return self.__colour

    def getMake(self):
        return self.__make

    def getMileage(self):
        return self.__mileage

    def setColour(self, colour):
        self.__colour = colour

    def setMake(self, make):
        self.__make = make

    def setMileage(self, mileage):
        self.__mileage = mileage

    def paint(self, colour):
        self.__colour = colour

    def move(self, distance):
        self.__mileage = self.__mileage + distance


class ElectricCar(Car):
    # The 1st function takes in all the functions/variables that make up Car and adds a new
    # variable called numberOfFuelCells.  As in Car getter and setters are used to access the object.
    # The electric car's will have 1 fuel cell as the default value.  While most cars have fuel cylinders
    # electric cars require fuel cells to run.

    def __init__(self):
        Car.__init__(self)
        self.__numberOfFuelCells = 1

    def getNumberOfFuelCells(self):
        return self.__numberOfFuelCells

    def setNumberOfFuelCells(self, value):
        self.__numberOfFuelCells = value


class PetrolCar(Car):
    # This class creates a petrol car object that is a sub class of car.  As in electric car
    # all functions/variables of car are brought in.  There is a difference in the unique functions
    # while an electric car has fuel cells, petrol cars have the numberOfFuelCylinders.  The
    # default number of cylinders is 3.  Getters and setters are used to get the numberOfFuelCylinders
    # variable and allows the user to set their own value for their own implementation without
    # changing the default value of the fuel cylinders.

    def __init__(self):
        Car.__init__(self)
        self.__numberOfFuelCylinders = 3

    def getNumberOfFuelCylinders(self):
        return self.__numberOfFuelCylinders

    def setNumberOfFuelCylinders(self, value):
        self.__numberOfFuelCylinders = value


class DieselCar(Car):
    # A DieselCar sub class of car is created.  It inherits all the functions/variables
    # from base class car.  Unlike PetorlCar which has a default of 3 cylinders, diesel will have
    # 5 as the default value.
    def __init__(self):
        Car.__init__(self)
        self.__numberOfFuelCylinders = 5

    def getNumberOfFuelCylinders(self):
        return self.__numberOfFuelCylinders

    def setNumberOfFuelCylinders(self, value):
        self.__numberOfFuelCylinders = value
