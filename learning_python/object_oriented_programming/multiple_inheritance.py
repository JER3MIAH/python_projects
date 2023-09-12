# multiple inheritance is a concept where a child class is derived from more than one parent class

class Prey:

    def flee(self):
        print("Run for your life")

class Predator:

    def hunt(self):
        print("Hunting mode activated")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):  # multiple parents
    pass

fish = Fish()

fish.hunt()
fish.flee()
