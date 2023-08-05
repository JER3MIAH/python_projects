# method overriding

class Animal:
    Alive = True

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):

    Alive = False
    def eat(self):
        print("This rabbit hops alot")

rabbit = Rabbit()
rabbit.eat()
rbbt = rabbit.Alive
print(rbbt)
# an object would use a method that is more closely associated with itself before relying on
# a method inherited from a parent class
