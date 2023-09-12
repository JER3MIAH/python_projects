# method chaining is used to call methods sequentially
# and each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("Turn the car on")
        return self

    def drive(self):
        print("Step on it !")
        return self

    def brake(self):
        print("Hit the brakes!")
        return self

    def turn_off(self):
        print("Turn the car off")
        return self

car = Car()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()  # it's important to return self so that this works
