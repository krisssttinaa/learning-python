from car import Car

#Car.wheels=2

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Audi", "RS7", 2020, "black")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()

print()

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_2.stop()

#car_1.wheels = 2