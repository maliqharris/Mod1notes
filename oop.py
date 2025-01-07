class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Whatup, i'm {self.name} and i'm {self.age} years old"
Maliq = Person("Maliq", 3000)
print(Maliq.greet())

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)        #-------------------Student class is pointing to the parent class of Person, it inherits
        self.student_id = student_id       #-------------------the name, and age from the parent class. The Student class is adding
                                           #-------------------the attribute of a student I.D to the person, the variable is named
Sponge = Student("Sponge", 22, "007")      #-------------------student_id , the is a demostration of object oriented programing. 
print(Sponge.greet())
print(Sponge.student_id)


class Car():
    def __init__(self, make, model, power):
        self.make = make 
        self.model = model
        self.power = power

Whitecar = Car("Tesla", 3, "Eletric")
Blackcar = Car("Hyndai", "Sonata", "Hybrid")

class Spec_car(Car):
    def __init__(self, make, model, power, year):
        super().__init__(make, model, power) #-----------------Super points to the parent class, specifically Spec_car is pointing to car
        self.year = year                     #-----------------and adding a year attribute. The original car has the make, model
    def greet(self):                         #-----------------and power originally.
        return f"Your car is a {self.make}, {self.power} powered, the model is a {self.model} from the year {self.year}"           
                                            
BMW = Spec_car("BMW", "325i", "Gas", 2003)


class house():
    def __init__(self, Doors, Windows, Rooms):
        self.windows = Windows
        self.doors= Doors
        self.rooms = Rooms

House_1 = house(3,10,6)

print(house.rooms)

print(BMW.year)  # works as intended.
print(BMW.make)  #OOp operations.
print(BMW.model)
print(BMW.power)
print(Sponge.student_id)
print(BMW.power)
print(BMW.greet())