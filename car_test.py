# The unittest library is imported to use its methods to test the program functionality.
# The various types of car are imported including the generic Car base class so the test
# class can use its functions.  First tests is on the generic Car base class and is called TestCar.

import unittest
from car import Car, ElectricCar, PetrolCar, DieselCar


class TestCar(unittest.TestCase):
	# unittest runs the test cases for the class.  TestCase is a subclass of the unit test class.
	# the setUp function uses the standard practice of naming the variable self to call itself.
    def setUp(self):
        self.car = Car()

    def test_car_mileage(self):
        # Function to test the mileage starts by testing 0 the default value called from the base class Car
		# move(15) calls the move method move which takes in the value in this case 15 and tests if the mileage
		# has increased by 15 which it has.
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())

    def test_car_make(self):
        # The default value for make is ' ' from the Car class so this is called.  The make is then set to Ferrari
		# tests that the value has successfully changed to Ferrari.
        self.assertEqual(' ', self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())

    def test_car_colour(self):
        # First the defualt value for colour of ' ' is tested called from the Car class.  Next the paint function is
		# used to test changing the colour of a car object.  In this case the car is painted red so the colour
		# becomes red which is tested next.
        self.assertEqual(' ', self.car.getColour())
        self.car.paint('red')
        self.assertEqual('red', self.car.getColour())


class TestElectricCar(unittest.TestCase):
	# The ElectricCar calls itslef using self.
	def setUp(self):
		self.electric_car = ElectricCar()

	def test_car_fuel_cells(self):
		# The default value for an electric car is called from the ElectricCar class which is 1 which is tested to
		# make sure the base class ElectricCar functions are being correctly implemented.  The setNumberOfFuelCells
		# is used to change the default value from 1 to 8, this is tested and it has become 8 so is true.  Note
		# set doesn't change default values held in base class.
		self.assertEqual(1, self.electric_car.getNumberOfFuelCells())
		self.electric_car.setNumberOfFuelCells(8)
		self.assertEqual(8, self.electric_car.getNumberOfFuelCells())

	def test_car_mileage(self):
		# As in the test_car_mileage 1st the default value is called this time from the ElectricCar class.
		# Move is then called using the value 15 is this is tested against the value retrieved from getMileage
		# which is 15 as well so it's true.
		self.assertEqual(0, self.electric_car.getMileage())
		self.electric_car.move(15)
		self.assertEqual(15, self.electric_car.getMileage())

class TestPetrolCar(unittest.TestCase):

	def setUp(self):
		# The ElectricCar calls itslef using self.
		self.petrol_car = PetrolCar()

	def test_car_fuel_cylinders(self):
		# Testing a PetrolCar the defaul value of 3 is called from the base class Petrol Car and is tested to
		# ensure the base class PetrolCar functions are being correctly implemented.  The setNumberOfFuelCylinders
		# in this case changes the default value from 3 to 7 this is tested and it has become 7 so is true.
		# This is similar to ElectricCar FuelCells implementation but with cylinders instead of cells.
		self.assertEqual(3, self.petrol_car.getNumberOfFuelCylinders())
		self.petrol_car.setNumberOfFuelCylinders(7)
		self.assertEqual(7, self.petrol_car.getNumberOfFuelCylinders())

	def test_car_mileage(self):
		# Ths function tests the mileage of the PetrolCar class.  As in the other tests it starts with the default
		# value from the base class.  Move is then called using the value 5 this is tested against the value
		# retrieved from getMileage which is now increased to 5 so it's true.
		self.assertEqual(0, self.petrol_car.getMileage())
		self.petrol_car.move(5)
		self.assertEqual(5, self.petrol_car.getMileage())

class TestDieselCar(unittest.TestCase):
	def setUp(self):
		# The DieselCar calls itslef using self.
		self.diesel_car = DieselCar()

	def test_car_fuel_cylinders(self):
		# This tests fuel_cylinders for a DieselCar class similar to a petrol car however the default value for
		# number of cylinders is higher for Diesel.  Then setNumberOfFuelCylinders method calls the function
		# from the base class DieselCar to change the value to 8.  This is tested and confirmed to be true.
		self.assertEqual(5, self.diesel_car.getNumberOfFuelCylinders())
		self.diesel_car.setNumberOfFuelCylinders(8)
		self.assertEqual(8, self.diesel_car.getNumberOfFuelCylinders())

	def test_car_mileage(self):
		# Function for testing the mileage of a DieselCar class.  As with other cars the default value is 0.
		# The move function is called taking the value 8.  This moves the car by 8km's.
		self.assertEqual(0, self.diesel_car.getMileage())
		self.diesel_car.move(8)
		self.assertEqual(8, self.diesel_car.getMileage())


if __name__ == '__main__':
    unittest.main()