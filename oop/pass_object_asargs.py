#pass objects as arguments

class Car:
    color = None

#paramentric
def change_color(vehicle, color):
    vehicle.color= color

car_1 = Car()

print(car_1.color)

change_color(car_1, "red")

print(car_1.color)