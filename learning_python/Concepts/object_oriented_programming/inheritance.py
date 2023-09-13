class Animal:  #parent clss

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):  #child class

    def run(self):
        print("This rabbit can hop")
class Fish(Animal):  #child class
    def swim(self):
        print("This fish swims fast")
class Hawk(Animal):  #child class
    def fly(self):
        print("This hawk can fly")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

hawk.fly()
rabbit.run()
fish.swim()
