from car import Car, ElectricCar, PetrolCar, DieselCar

red_car = Car()
print 'Colour ' + red_car.getColour()
print 'Mileage ' + str(red_car.getMileage())
print 'Make ' + red_car.getMake()

red_car.setMake('Ferrari')
print 'Make ' + red_car.getMake()
print('Getting a paint job - the new colour is ' + str(red_car.paint('red')))
print 'Colour ' + red_car.getColour()

red_car.move(15)
print 'Mileage ' + str(red_car.getMileage())
print 'Engine Size ' + red_car.engineSize
red_car.engineSize = '3.9'
print 'Engine Size ' + red_car.engineSize


car3 = ElectricCar()
car3.setColour('White')
car3.setMileage(500)
print('\ncar3 the mileage is ' + str(car3.getMileage()))
car3.setNumberOfFuelCells(2)
car3.move(20)
print('The mileage is now ' + str(car3.getMileage()))
car3.engineSize = '3.1'
print('car3 colour: ' + car3.getColour())
print('car3 numberFuelCells: ' + str(car3.getNumberOfFuelCells()))
print 'Engine Size ' + car3.engineSize


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

    def create_current_stock(self):
        for i in range(20):
           self.electric_cars.append(ElectricCar())
        for i in range(15):
           self.petrol_cars.append(PetrolCar())
        for i in range(10):
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