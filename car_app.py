# 1st I am importing all the car class' from Car, next a welcome message for the rental service is displayed
# to the user.  red_car is the name of the 1st object that takes in the functions from the generic Car base class.
# DBS Car Rental is the name of the client so they will appear on the welcome message.

from car import Car, ElectricCar, PetrolCar, DieselCar

print 'Welcome to DBS Car Rental below is a list of available cars and the car details\n.'
red_car = Car()

# setMake calls the function from the Car class with the same name.  It has 2 variables self and make.  I
# am passing in the string Ferrari as the value for make.  This allows the app program to set a value
# without changing the structure or default value for any variables.  getMake calls the function of the same
# name in Car and returns the value of make which is added to the end of the print statement.
# The paint function of the Car class is called which is passed the value red so the default value ' ' isn't used.
# The getColour functions returns the value being stored in colour for red_car which is now red which is printed.
red_car.setMake('Ferrari')
print 'Our most exclusive offer is a ' + red_car.getMake()

red_car.paint('red')
print 'The colour is ' + red_car.getColour()

# The move function passes the value 15 to the Car class and in the move function adds it to the value held in
# mileage this is used to create the new mileage figure and is printed to the screen.
# The default value for engineSize is ' '.  For the red_car I am assigning it the value 3.7.  The value of
# engineSize can be changed to any number without changing the Car class.
red_car.move(15)
print 'The mileage is ' + str(red_car.getMileage()) + 'kms'

red_car.engineSize = '3.7'
print 'The engine Size is ' + red_car.engineSize

# A ElectricCar object is called by car2 and can now use the functions of an ElectricCar class.  Similar functionality
# as red_car in make function.  # Unlike the red_car which used the paint function here I am using the setColour
# function which takes in self and colour as variables in this case while.  The getColour function returns the value
# held in colour.  In this case the value of colour was changed from ' ' to White which is displayed to the user.
car2 = ElectricCar()
car2.setMake('Nissan LEAF')
print 'Our environment friendly option ' + car2.getMake()

car2.setColour('White')
print('The colour is ' + car2.getColour())

# Similar functionality in mileage, move and engineSize except in this case Mileage is at 300 instead of the
# default value of 0.  This results in the mileage starting at 300 and becoming 320 after the move function.
# Unlike petrol and diesel cars which have fuel cylinders electric cars require fuel cells to run.  The function
# setNumberOfFuelCells takes in 2 values self and the value for fuel cells in this case 2.  The next line prints
# an appropriate message and uses the getNumberOfFuelCells which returns the value held in the variable which is 2.
car2.setMileage(300)
car2.move(20)
print('The mileage is ' + str(car2.getMileage()))
car2.engineSize = '3.1'
print 'The engine Size is ' + car2.engineSize

car2.setNumberOfFuelCells(2)
print('The number of fuel cells is ' + str(car2.getNumberOfFuelCells()))


car4 = PetrolCar()
car4.setColour('Blue')
car4.setMileage(800)
car4.setNumberOfFuelCylinders(3)
car4.move(20)
print('\ncar4 colour: ' + car4.getColour())
print('car4 numberFuelCylinders: ' + str(car4.getNumberOfFuelCylinders()))

car5 = DieselCar()
car5.setColour('Green')
car5.setMileage(1000)
car5.setNumberOfFuelCylinders(5)
car5.move(20)
print('\ncar5 colour: ' + car5.getColour())
print('car5 numberFuelCylinders: ' + str(car5.getNumberOfFuelCylinders()))

class Dealership(object):

    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []

    # 40 cars: 60% petrol (24 cars), 20% diesel (8 cars), 10% electric (4 cars) and 10% hybrid (4 cars).
    def create_current_stock(self):
        for i in range(4):
           self.electric_cars.append(ElectricCar())
        for i in range(24):
           self.petrol_cars.append(PetrolCar())
        for i in range(8):
            self.diesel_cars.append(DieselCar())

    def stock_count(self):	
        print 'Petrol cars in stock ' + str(len(self.petrol_cars))
        print 'Electric cars in stock ' + str(len(self.electric_cars))
        print 'Diesel cars in stock ' + str(len(self.diesel_cars))


    def rent(self, car_list, amount):
        if len(car_list) < amount:
            print 'Not enough cars in stock'
            return
        total = 0
        while total < amount:
            car_list.pop()
            total = total + 1

    def process_car_rental(self):
        answer = raw_input('Would you like to rent a car? yes/no\n')
        if answer == 'yes' or answer == 'y':
            answer = raw_input('What type would you like? petrol/diesel/electric\n')
            amount = int(raw_input('How many would you like?\n'))
            if answer == 'petrol' or answer == 'p':
                self.rent(self.petrol_cars, amount)
                self.stock_count()
                
            elif answer == 'diesel' or answer == 'd':
                self.rent(self.diesel_cars, amount)
                self.stock_count()

            else:
                self.rent(self.electric_cars, amount)
                self.stock_count()


dealership = Dealership()
dealership.create_current_stock()
dealership.stock_count()
proceed = 'y'

while proceed == 'yes' or proceed == 'y':
    dealership.process_car_rental()
    proceed = raw_input('Would you like to rent more car(s)? yes/no\n')