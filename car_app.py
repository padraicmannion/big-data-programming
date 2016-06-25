# 1st I am importing all the car class' from Car, next a welcome message for the rental service is displayed
# to the user.  red_car is the name of the 1st object that takes in the functions from the generic Car base class.
# DBS Car Rental is the name of the client so they will appear on the welcome message.

from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar

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
print '\nOur environment friendly option is ' + car2.getMake()

car2.setColour('White')
print('The colour is ' + car2.getColour())

# Similar functionality in mileage, move and engineSize except in this case Mileage is at 300 instead of the
# default value of 0.  This results in the mileage starting at 300 and becoming 320 after the move function.
# Unlike petrol and diesel cars which have fuel cylinders electric cars require fuel cells to run.  The function
# setNumberOfFuelCells takes in 2 values self and the value for fuel cells in this case 2.  The next line prints
# an appropriate message and uses the getNumberOfFuelCells which returns the value held in the variable which is 2.
car2.setMileage(300)
car2.move(20)
print('The mileage is ' + str(car2.getMileage())) + 'kms'
car2.engineSize = '2.1'
print 'The engine Size is ' + car2.engineSize

car2.setNumberOfFuelCells(2)
print('The number of fuel cells is ' + str(car2.getNumberOfFuelCells()))


# A HybridCar Class is called by car3 allowing it to use the functions and variables of the class.  A hybrid is
# 1 part standard motor car and 1 part electric car so it will use a cylinder and a cell function.  The make
# takes in the value Toyota Prius and prints a message to the user.  The colour is set at blue and printed.
# Same functionality as other mileage in this case 100 is the value that is set, next 17 is added using move
# resulting in a value of 117kms.  The engineSize variable is set as 3.1.  Hybrid cars require both cells and
# cylinders so it will use both functions.
car3 = HybridCar()
car3.setMake('Toyota Prius')
print '\nOur hybrid option is ' + car3.getMake()

car3.setColour('Blue')
print('The colour is ' + car3.getColour())

car3.setMileage(100)
car3.move(17)
print('The mileage is ' + str(car3.getMileage())) + 'kms'
car3.engineSize = '3.1'
print 'The engine Size is ' + car3.engineSize

car3.setNumberOfFuelCells(2)
print('The number of fuel cells is ' + str(car3.getNumberOfFuelCells()))
car3.setNumberOfFuelCylinders(1)
print('The number of fuel cylinders is ' + str(car3.getNumberOfFuelCylinders()))


# Car4 calls the PetrolCar class and performs similar functions as other class'.  The colour is red, mileage
# is set to 150 and increased by 25 to 175kms.  The engine size is set at 2.9.  The petrol car is a Toyota Corolla
# and has 3 cylinders set as the value for the variable NumberOfFuelCylinders.
car4 = PetrolCar()
car4.setMake('Toyota Corolla')
print '\nOur petrol option is ' + car4.getMake()

car4.setColour('Red')
print('The colour is: ' + car4.getColour())

car4.setMileage(150)
car4.move(25)
print('The mileage is ' + str(car4.getMileage())) + 'kms'
car4.engineSize = '2.9'
print 'The engine Size is ' + car4.engineSize

car4.setNumberOfFuelCylinders(3)
print('The number of fuel cylinders is ' + str(car4.getNumberOfFuelCylinders()))


# Car5 is calling a DieselCar objects and will implement its functions and variables.  Similar to other class'
# the car sets a model and returns it in this case Mercedes Benz, the colour is set as silver, the mileage is
# 1000 and increased by 40 to 1040 as the mileage returned, the engineSize is 3.2 and the car uses 5 cylinders.
car5 = DieselCar()
car5.setMake('Mercedes Benz')
print '\nOur diesel option is ' + car4.getMake()

car5.setColour('Silver')
print('The colour is ' + car5.getColour())

car5.setMileage(1000)
car5.move(40)
print('The mileage is ' + str(car5.getMileage())) + 'kms'
car5.engineSize = '3.2'
print 'The engine Size is ' + car5.engineSize

car5.setNumberOfFuelCylinders(5)
print('The number of fuel cylinders is ' + str(car5.getNumberOfFuelCylinders()))

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