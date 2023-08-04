class Car:

    wheels = 4  # class variable

    def __init__(self, make, model, year, color):
        self.make = make  # attributes
        self.model = model  # these are |instance variables|
        self.year = year
        self.color = color

    def drive(self):   # methods
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" has stopped")

