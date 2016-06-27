# The unittest library is imported to use its methods to test the program functionality.
# The various types of car are imported including the generic Car base class so the test
# class can use its functions.  First tests are on the generic Car base class and is called TestCar.

import unittest
from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car()
        # unittest runs the test cases for the class.  TestCase is a subclass of the unit test class.
        # the setUp function uses the standard practice of naming the variable self to call itself.
        # def setUp(self):

    def test_car_mileage_and_move(self):
        # Function to test the mileage starts by testing 0 the default value called from the base class Car
        # move(15) calls the move method move which takes in the value in this case 15 and tests if the mileage
        # has increased by 15 which it has, 12 is added to make 27, than 13 to make 40 than 3.5 to make 43.5.  0
        # is tested and finally changing the value of mileage using setMileage is tested with the value 20 which is
        # passed to the function in the Car class this is tested and the change is confirmed mileage is 20.
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())
        self.car.move(12)
        self.assertEqual(27, self.car.getMileage())
        self.car.move(13)
        self.assertEqual(40, self.car.getMileage())
        self.car.move(3.5)
        self.assertEqual(43.5, self.car.getMileage())
        self.car.move(0)
        self.assertEqual(43.5, self.car.getMileage())
        self.car.setMileage(20)
        self.assertEqual(20, self.car.getMileage())

    def test_car_make(self):
        # The default value for make is ' ' from the Car class so this is called.  The make is set to Ferrari
        # tests that the value has successfully changed to Ferrari.  Next it is set to Ford and finally Honda Civic.
        self.assertEqual(' ', self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())
        self.car.setMake('Ford')
        self.assertEqual('Ford', self.car.getMake())
        self.car.setMake('Honda Civic')
        self.assertEqual('Honda Civic', self.car.getMake())

    def test_car_engineSize(self):
        # The default engineSize value is ' ' so this is tested first followed by 1.8 and 3.0
        self.assertEqual(' ', self.car.getEngineSize())
        self.car.setEngineSize(1.8)
        self.assertEqual(1.8, self.car.getEngineSize())
        self.car.setEngineSize(3.0)
        self.assertEqual(3.0, self.car.getEngineSize())

    def test_car_colour_and_paint(self):
        # First the default value for colour of ' ' is tested called from the Car class.  Next the paint function is
        # used to test changing the colour of a car object.  In this case the car is painted red so the colour
        # becomes red which is tested next.  The paint function is applied using blue and finally the setColour method
        # of the Car class that takes in the value green in this case using the getColour method which returns the
        # value held in colour and tests it against the string which is correct.
        self.assertEqual(' ', self.car.getColour())
        self.car.paint('red')
        self.assertEqual('red', self.car.getColour())
        self.car.paint('blue')
        self.assertEqual('blue', self.car.getColour())
        self.car.setColour('green')
        self.assertEqual('green', self.car.getColour())


class TestElectricCar(unittest.TestCase):
    # The ElectricCar calls itself using self.
    def setUp(self):
        self.electric_car = ElectricCar()

    def test_electricCar_fuel_cells(self):
        # The default value for an electric car is called from the ElectricCar class which is 2 which is tested to
        #  make sure the base class ElectricCar functions are being correctly implemented.  The setNumberOfFuelCells
        # is used to change the default value from 2 to 8, this is tested and it has become 8 so is true.  5 and 7
        # are then placed as testing values for getNumberofFuelCells.  Note set doesn't change default values held
        # in base class.
        self.assertEqual(2, self.electric_car.getNumberOfFuelCells())
        self.electric_car.setNumberOfFuelCells(8)
        self.assertEqual(8, self.electric_car.getNumberOfFuelCells())
        self.electric_car.setNumberOfFuelCells(5)
        self.assertEqual(5, self.electric_car.getNumberOfFuelCells())
        self.electric_car.setNumberOfFuelCells(7)
        self.assertEqual(7, self.electric_car.getNumberOfFuelCells())

    def test_electricCar_mileage_and_move(self):
        # I am testing mileage and move for all cars to ensure correct implementation and because mileage is
        # an important factor for NCT tests and how many kilometers are on the clock.
        # As in the test_car_mileage 1st the default value is called this time from the ElectricCar class.
        # Move is then called using the value 15 is this is tested against the value retrieved from getMileage
        # which is 15 as well so it's true.  Mileage is then increased by 6.5 to 21.5.  Next the setMileage function
        # calls the function from the ElectricCar class which has inherited all the functions of the base class Car.
        # All the types of cars have inherited all the functions of Car.  In this case SetMileage is called and
        # takes the value 40.  This is tested using the getMileage function to ensure it's changed to 40 and it has.
        # The value 0 is tested and mileage variable remains 40.
        self.assertEqual(0, self.electric_car.getMileage())
        self.electric_car.move(15)
        self.assertEqual(15, self.electric_car.getMileage())
        self.electric_car.move(6.5)
        self.assertEqual(21.5, self.electric_car.getMileage())
        self.electric_car.setMileage(40)
        self.assertEqual(40, self.electric_car.getMileage())
        self.electric_car.move(0)
        self.assertEqual(40, self.electric_car.getMileage())

    def test_electricCar_make(self):
        # Even though make, engineSize, colour and paint are tested in the base class I feel it's important to
        # have test cases for the subclass' that implement the functions to ensure they are correctly inherited
        # with the same functionality so the default value ' ' is tested, a string with 1 word and a string with
        # 2 words.  Also i'm not using car.getMake but electric_car.getMake this will be the case in the other
        # subclass' where the functions are implemented from the subclass not the superclass/base class.
        self.assertEqual(' ', self.electric_car.getMake())
        self.electric_car.setMake('Charger')
        self.assertEqual('Charger', self.electric_car.getMake())
        self.electric_car.setMake('Super Charger')
        self.assertEqual('Super Charger', self.electric_car.getMake())

    def test_electricCar_engineSize(self):
        # Testing engineSize for ElectricCar class.
        self.assertEqual(' ', self.electric_car.getEngineSize())
        self.electric_car.setEngineSize(1.2)
        self.assertEqual(1.2, self.electric_car.getEngineSize())
        self.electric_car.setEngineSize(0.8)
        self.assertEqual(0.8, self.electric_car.getEngineSize())

    def test_electricCar_colour_and_paint(self):
        # Testing colour and paint for ElectricCar
        self.assertEqual(' ', self.electric_car.getColour())
        self.electric_car.paint('pink')
        self.assertEqual('pink', self.electric_car.getColour())
        self.electric_car.paint('orange')
        self.assertEqual('orange', self.electric_car.getColour())
        self.electric_car.setColour('yellow')
        self.assertEqual('yellow', self.electric_car.getColour())


class TestPetrolCar(unittest.TestCase):

    def setUp(self):
        # The PetrolCar class calls itself.
        self.petrol_car = PetrolCar()

    def test_PetrolCar_fuel_cylinders(self):
        # Testing a PetrolCar the default value of 3 is called from the base class Petrol Car and is tested to
        # ensure the base class PetrolCar functions are being correctly implemented.  The setNumberOfFuelCylinders
        # in this case changes the default value from 3 to 7 this is tested and it has become 7 so is true.
        # This is similar to ElectricCar FuelCells implementation but with cylinders instead of cells.
        # The cylinders are tested with values for 2 and 5 which pass.
        self.assertEqual(3, self.petrol_car.getNumberOfFuelCylinders())
        self.petrol_car.setNumberOfFuelCylinders(7)
        self.assertEqual(7, self.petrol_car.getNumberOfFuelCylinders())
        self.petrol_car.setNumberOfFuelCylinders(2)
        self.assertEqual(2, self.petrol_car.getNumberOfFuelCylinders())
        self.petrol_car.setNumberOfFuelCylinders(5)
        self.assertEqual(5, self.petrol_car.getNumberOfFuelCylinders())

    def test_PetrolCar_mileage_and_move(self):
        # Ths function tests the mileage of the PetrolCar class.  As in the other tests it starts with the default
        # value from the base class.  Move is then called using the value 5 this is tested against the value
        # retrieved from getMileage which is now increased to 5 so it's true.  It is increased by 12 to make 17,
        # tested by adding 0 still gives 17, tested adding a decimal 6.5 to get 23.5.
        self.assertEqual(0, self.petrol_car.getMileage())
        self.petrol_car.move(5)
        self.assertEqual(5, self.petrol_car.getMileage())
        self.petrol_car.move(12)
        self.assertEqual(17, self.petrol_car.getMileage())
        self.petrol_car.move(0)
        self.assertEqual(17, self.petrol_car.getMileage())
        self.petrol_car.move(6.5)
        self.assertEqual(23.5, self.petrol_car.getMileage())

    def test_PetrolCar_make(self):
        # Testing make function for PetrolCar to ensure correctly inherited from base class Car.
        self.assertEqual(' ', self.petrol_car.getMake())
        self.petrol_car.setMake('Ford')
        self.assertEqual('Ford', self.petrol_car.getMake())
        self.petrol_car.setMake('Ford Focus')
        self.assertEqual('Ford Focus', self.petrol_car.getMake())

    def test_PetrolCar_engineSize(self):
        # Testing engineSize for PetrolCar class.
        self.assertEqual(' ', self.petrol_car.getEngineSize())
        self.petrol_car.setEngineSize(2.2)
        self.assertEqual(2.2, self.petrol_car.getEngineSize())
        self.petrol_car.setEngineSize(2.6)
        self.assertEqual(2.6, self.petrol_car.getEngineSize())

    def test_PetrolCar_colour_and_paint(self):
        # Testing colour and paint for PetrolCar Class
        self.assertEqual(' ', self.petrol_car.getColour())
        self.petrol_car.paint('black')
        self.assertEqual('black', self.petrol_car.getColour())
        self.petrol_car.setColour('dark blue')
        self.assertEqual('dark blue', self.petrol_car.getColour())


class TestDieselCar(unittest.TestCase):
    def setUp(self):
        # The DieselCar calls itself using self.
        self.diesel_car = DieselCar()

    def test_DieselCar_fuel_cylinders(self):
        # This tests fuel_cylinders for a DieselCar class similar to a petrol car however the default value for
        # number of cylinders is higher for diesel.  Then setNumberOfFuelCylinders method calls the function
        # from the base class DieselCar to change the value to 8.  This is tested and confirmed to be true.
        # The next tests test cylinders for the values 2 and 4 which are confirmed in the test cases as true.
        self.assertEqual(5, self.diesel_car.getNumberOfFuelCylinders())
        self.diesel_car.setNumberOfFuelCylinders(8)
        self.assertEqual(8, self.diesel_car.getNumberOfFuelCylinders())
        self.diesel_car.setNumberOfFuelCylinders(2)
        self.assertEqual(2, self.diesel_car.getNumberOfFuelCylinders())
        self.diesel_car.setNumberOfFuelCylinders(4)
        self.assertEqual(4, self.diesel_car.getNumberOfFuelCylinders())

    def test_DieselCar_mileage_and_move(self):
        # Function for testing the mileage of a DieselCar class.  As with other cars the default value is 0.
        # The move function is called taking the value 8.  This moves the car by 8km's.  Next it is increased
        # by 20 to make 28, tested with increasing by 0 and remains 28.  The setMileage function calls the function
        # in the DieselCar class which inherits the function from the Car class.  This sets mileage at 30 which is
        # tested and is true and lastly move by 7.5 to increase mileage to 37.5 which is tested and is true.
        self.assertEqual(0, self.diesel_car.getMileage())
        self.diesel_car.move(8)
        self.assertEqual(8, self.diesel_car.getMileage())
        self.diesel_car.move(20)
        self.assertEqual(28, self.diesel_car.getMileage())
        self.diesel_car.move(0)
        self.assertEqual(28, self.diesel_car.getMileage())
        self.diesel_car.setMileage(30)
        self.assertEqual(30, self.diesel_car.getMileage())
        self.diesel_car.move(7.5)
        self.assertEqual(37.5, self.diesel_car.getMileage())

    def test_DieselCar_make(self):
        # Testing make function for DieselCar.
        self.assertEqual(' ', self.diesel_car.getMake())
        self.diesel_car.setMake('Chevy')
        self.assertEqual('Chevy', self.diesel_car.getMake())
        self.diesel_car.setMake('Chevy Impala')
        self.assertEqual('Chevy Impala', self.diesel_car.getMake())
        self.diesel_car.setMake('Chevrolet Silverado 2500 HD')
        self.assertEqual('Chevrolet Silverado 2500 HD', self.diesel_car.getMake())

    def test_DieselCar_engineSize(self):
        # Testing engineSize for DieselCar class.
        self.assertEqual(' ', self.diesel_car.getEngineSize())
        self.diesel_car.setEngineSize(3.3)
        self.assertEqual(3.3, self.diesel_car.getEngineSize())
        self.diesel_car.setEngineSize(3.5)
        self.assertEqual(3.5, self.diesel_car.getEngineSize())

    def test_DieselCar_colour_and_paint(self):
        # Testing colour and paint for DieselCar Class.
        self.assertEqual(' ', self.diesel_car.getColour())
        self.diesel_car.paint('silver')
        self.assertEqual('silver', self.diesel_car.getColour())
        self.diesel_car.setColour('white')
        self.assertEqual('white', self.diesel_car.getColour())

    class TestHybridCar(unittest.TestCase):
        def setUp(self):
            # The HybridCar calls itself using self.
            self.hybrid_car = HybridCar()

        def test_HybridCar_fuel_cylinders(self):
            # Similar to petrol and diesel except default value is 1.  The default value is tested as well as 4, 6
            # and 3 which all result in true.
            self.assertEqual(1, self.hybrid_car.getNumberOfFuelCylinders())
            self.hybrid_car.setNumberOfFuelCylinders(4)
            self.assertEqual(4, self.hybrid_car.getNumberOfFuelCylinders())
            self.hybrid_car.setNumberOfFuelCylinders(6)
            self.assertEqual(6, self.hybrid_car.getNumberOfFuelCylinders())
            self.hybrid_car.setNumberOfFuelCylinders(3)
            self.assertEqual(3, self.hybrid_car.getNumberOfFuelCylinders())

        def test_HybridCar_fuel_cells(self):
            # Similar to ElectricCar test_car_fuel_cells.  The default value 1 is tested as well as 4 and 2.
            self.assertEqual(1, self.hybrid_car.getNumberOfFuelCells())
            self.hybrid_car.setNumberOfFuelCells(4)
            self.assertEqual(4, self.hybrid_car.getNumberOfFuelCells())
            self.hybrid_car.setNumberOfFuelCells(2)
            self.assertEqual(2, self.hybrid_car.getNumberOfFuelCells())

        def test_HybridCar_mileage_and_move(self):
            # As in other cases testing the mileage default value.  Then entering a value for move to ensure
            # it moves that amount to test the mileage of a car.  The car is moved by 7.7 to make 19.7 moved 0
            # output stays the same and lastly setMileage is tested with a value of 15 which is true.
            self.assertEqual(0, self.hybrid_car.getMileage())
            self.hybrid_car.move(12)
            self.assertEqual(12, self.hybrid_car.getMileage())
            self.hybrid_car.move(7.7)
            self.assertEqual(19.7, self.hybrid_car.getMileage())
            self.hybrid_car.move(0)
            self.assertEqual(19.7, self.hybrid_car.getMileage())
            self.hybrid_car.setMileage(15)
            self.assertEqual(15, self.hybrid_car.getMileage())

        def test_HybridCar_make(self):
            # Testing make function for HybridCar.
            self.assertEqual(' ', self.hybrid_car.getMake())
            self.hybrid_car.setMake('Chevrolet Malibu')
            self.assertEqual('Chevrolet Malibu', self.hybrid_car.getMake())
            self.hybrid_car.setMake('Chevrolet Cruz')
            self.assertEqual('Chevrolet Cruz', self.hybrid_car.getMake())

        def test_HybridCar_engineSize(self):
            # Testing engineSize for HybridCar.
            self.assertEqual(' ', self.hybrid_car.getEngineSize())
            self.hybrid_car.setEngineSize(1.6)
            self.assertEqual(1.6, self.hybrid_car.getEngineSize())
            self.hybrid_car.setEngineSize(1.8)
            self.assertEqual(1.8, self.hybrid_car.getEngineSize())

        def test_HybridCar_colour_and_paint(self):
            # Testing colour and paint for HybridCar.
            self.assertEqual(' ', self.hybrid_car.getColour())
            self.hybrid_car.paint('red')
            self.assertEqual('red', self.hybrid_car.getColour())
            self.hybrid_car.setColour('light blue')
            self.assertEqual('light blue', self.hybrid_car.getColour())

# Runs all the test cases.
if __name__ == '__main__':
    unittest.main()