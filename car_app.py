from car import Car, ElectricCar, PetrolCar

red_car = Car()
print 'Colour ' + red_car.getColour()
print 'Mileage ' + str(red_car.getMileage())
print 'Make ' + red_car.getMake()

red_car.setMake('Ferrari')

print 'Make ' + red_car.getMake()

red_car.paint('red')
print 'Colour ' + red_car.getColour()

red_car.move(15)
print 'Mileage ' + str(red_car.getMileage())

print 'Engine Size ' + red_car.engineSize
red_car.engineSize = '3.9'
print 'Engine Size ' + red_car.engineSize

car3 = ElectricCar()
car3.setColour('White')
car3.setMileage(500)
car3.setNumberOfFuelCells(2)
car3.move(20)
print('car3 colour: ' + car3.getColour())
print('car3 numberFuelCells: ' + str(car3.getNumberOfFuelCells()))

class Dealership(object):

	def __init__(self):
		self.electric_cars = []
		self.petrol_cars = []

    for i in range(20):
        cars.append(ElectricCar())
    for i in range(15):
        cars.append(PetrolCar())

    def stock_count():	
        print 'petrol cars in stock ' + str(len(petrol_cars))
        print 'electric cars cars in stock ' + str(len(electric_cars))

    def rent(car_list, amount):
        if len(car_list) < amount:
            print 'Not enough cars in stock'
            return
        total = 0
        while total < amount:
            car_list.pop()
            total = total + 1
        petrol_cars.pop()

    def process_car_rental(self)
        answer = raw_input('Would you like to rent a yar? y/n')
        if answer == 'y':
            answer = raw_input('what type would you like? p/d')
            amount = int(raw_input('how many would you like?'))
        if answer == 'p':
            self.rent(self.petrol_cars, amount)
        else:
            self.rent(self.electric_cars, amount)
            self.stock_count()

dealership = Dealership()
dealership.create_current_stock()
dealership.stock_count()		
proceed = 'y'
while proceed == 'y':
    dealership.process_rental()
    proceed = raw_input('continue? y/n')

car4 = PetrolCar()
car4.setColour('Blue')
car4.setMileage(800)
car4.setNumberOfFuelCylinders(3)
car4.move(20)
print('car4 colour: ' + car4.getColour())
print('car4 numberFuelCylinders: ' + str(car4.getNumberOfFuelCylinders()))

car5 = DieselCar()
car5.setColour('Green')
car5.setMileage(1000)
car5.setNumberOfFuelCylinders(5)
car5.move(20)
print('car5 colour: ' + car5.getColour())
print('car5 numberFuelCylinders: ' + str(car5.getNumberOfFuelCylinders()))
