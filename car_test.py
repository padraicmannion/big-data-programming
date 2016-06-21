import unittest
from car import Car, ElectricCar, PetrolCar, DieselCar
# The unittest library is imported to use its methods to test the program functionality.
# The various types of car are imported including the generic Car base class so the test
# class can use its functions.  First tests is on the generic car base class and is called TestCar.

class TestCar(unittest.TestCase):

    def setUp(self): 
        self.car = Car()  
        # unittest runs the test cases for the class.  TestCase is a subclass of the unit test class. 
        # the setUp function uses the standard practice of naming the variable self to call itself.

    def test_car_mileage(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())
        # Function to test the mileage move(15) moves the car 15km's therefore the mileage
        # should have also increased by 15.

    def test_car_make(self):
        self.assertEqual(' ', self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())
        # Set the make of the car to Ferrari and store it in the variable make.

    def test_car_colour(self):
        self.assertEqual(' ', self.car.getColour())
        self.car.paint('red')
        self.assertEqual('red', self.car.getColour())
        # Testing the paint function by painting the car red as it's a Ferrari.

class TestElectricCar(unittest.TestCase):
	def setUp(self):
		self.electric_car = ElectricCar()

	def test_car_fuel_cells(self):
		self.assertEqual(1, self.electric_car.getNumberOfFuelCells())
		self.electric_car.setNumberOfFuelCells(8)
		self.assertEqual(8, self.electric_car.getNumberOfFuelCells())

	def test_car_mileage(self):
		self.assertEqual(0, self.electric_car.getMileage())
		self.electric_car.move(15)
		self.assertEqual(15, self.electric_car.getMileage())

class TestPetrolCar(unittest.TestCase):
	def setUp(self):
		self.petrol_car = PetrolCar()

	def test_car_fuel_cylinders(self):
		self.assertEqual(3, self.petrol_car.getNumberOfFuelCylinders())
		self.petrol_car.setNumberOfFuelCylinders(8)
		self.assertEqual(8, self.petrol_car.getNumberOfFuelCylinders())

	def test_car_mileage(self):
		self.assertEqual(0, self.petrol_car.getMileage())
		self.petrol_car.move(15)
		self.assertEqual(15, self.petrol_car.getMileage())

class TestDieselCar(unittest.TestCase):
	def setUp(self):
		self.diesel_car = DieselCar()

	def test_car_fuel_cylinders(self):
		self.assertEqual(5, self.diesel_car.getNumberOfFuelCylinders())
		self.diesel_car.setNumberOfFuelCylinders(8)
		self.assertEqual(8, self.diesel_car.getNumberOfFuelCylinders())

	def test_car_mileage(self):
		self.assertEqual(0, self.diesel_car.getMileage())
		self.diesel_car.move(15)
		self.assertEqual(15, self.diesel_car.getMileage())


if __name__ == '__main__':
    unittest.main()