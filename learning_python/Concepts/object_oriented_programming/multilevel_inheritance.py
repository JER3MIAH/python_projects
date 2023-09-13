# multilevel inheritance is a concept where a child(derived) class inherits from another child(derived) class

class Beings:

    alive = True

class Animal(Beings):

    def eat(self):
        print("This dog eats well")

class Dog(Animal):

    def bark(self):
        print("This dog sure barks alot")

dog = Dog()
animal = Animal()
beings = Beings()

print(dog.alive)   # inherited from the Beings class
dog.eat()          # inherited from the Animal class
dog.bark()         # defined in the dog class
