
import unittest
from car import Car, ElectricCar, PetrolCar, DieselCar


class TestCar(unittest.TestCase):

    def setUp(self): 
        self.car = Car()
    
    def test_car_mileage(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())
        
    def test_car_make(self):
        self.assertEqual(' ', self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())
        
    def test_car_colour(self):
        self.assertEqual(' ', self.car.getColour())
        self.car.paint('red')
        self.assertEqual('red', self.car.getColour())
		
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