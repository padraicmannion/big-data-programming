# define a class for a car

class Car(object):
    # implement car object
    def __init__(self):
       self.__colour = ' '
       self.__make = ' '
       self.__mileage = 0
       self.engineSize = ' '
       # init is a name used for when the fields need to be made private (naming convention)
       # although in python it's not really possible to have a truly private function, class
       # etc because it's not Pythonic.  The class Car inherits from the object base class.
       # A car has the variables colour, make, mileage and engineSize for the car base class.
       # By using a single or double _ before the variable name defines it as private.
       # Private protects the variables from change and means anyone can implement them using
       # getters and setters without changing the base object. 
       
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
        print('Getting a paint job - the new colour is ' + colour)
        self.__colour = colour
        
    def move(self, distance):
        print('Moving the car ' + str(distance) + 'kms')
        self.__mileage = self.__mileage + distance
        
    # Getter and setter methods can be implemented in new and different ways and add new
    # functions, variables or functionality etc.  The paint job updates the colour of the specific
    # car object without changing the value held in the private variable.  The move is used to test
    # the car for example 15km's that should make the mileage of the car in turn increase by 15.

class ElectricCar(Car):

	def __init__(self):
		Car.__init__(self)
		self.__numberOfFuelCells = 1
		
	def getNumberOfFuelCells(self):
		return self.__numberOfFuelCells
		
	def setNumberOfFuelCells(self, value):
		self.__numberOfFuelCells = value
        
    # The 1st function takes in all the functions/variables that make up Car and adds a new
    # variable called numberOfFuelCells.  As in Car getter and setters are used to access the object.
		
class PetrolCar(Car):

	def __init__(self):
		Car.__init__(self)
		self.__numberOfFuelCylinders = 3
		
	def getNumberOfFuelCylinders(self):
		return self.__numberOfFuelCylinders
		
	def setNumberOfFuelCylinders(self, value):
		self.__numberOfFuelCylinders = value
		
class DieselCar(Car):

	def __init__(self):
		Car.__init__(self)
		self.__numberOfFuelCylinders = 5
		
	def getNumberOfFuelCylinders(self):
		return self.__numberOfFuelCylinders
		
	def setNumberOfFuelCylinders(self, value):
		self.__numberOfFuelCylinders = value