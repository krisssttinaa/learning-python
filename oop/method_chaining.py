# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self

class Car:
    def turn_on(self):
        print("You start the engine")
        return self
    
    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()

#car.turn_on()
#car.drive()

#chaining - to use it like that u have to add return self, so that it passes itself to next method
car.turn_on().drive()
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()

