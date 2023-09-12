# an object is an instance of a class
# with programming, we can mimic real world objects by assigning a combo of attributes
# and methods (methods = what an object does, attribute = what an object is or has)

from OOP2 import Car

first_car = Car("Toyota", "Camry", 2020, "Black")
second_car = Car("Range", "Rover", 2023, "Blue")

print(second_car.make)
print(second_car.model)
print(second_car.year)
print(second_car.color)

first_car.drive()
second_car.stop()


