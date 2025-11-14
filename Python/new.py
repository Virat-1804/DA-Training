#importing other file

"""import person #importing other file

print(person.greet("Virat"))"""

#random module

"""import random

print("Random number between 1-100 : ", random.randint(1,100))
colors = ["red", "grey", "violet"]
print("Random color: ",random.choice(colors))"""

#date and time module

"""import datetime

today = datetime.date.today()
print("Today's date:", today)

now = datetime.datetime.now()
print("Current time:", now)"""

#sys module

"""import sys

print("Python version:", sys.version)
print("Platform:", sys.platform)"""

#math module

"""import math

print("Square root of 49:", math.sqrt(49))
print("value of pi:", math.pi)
print("Ceil of 6.9:", math.ceil(6.9))
print("Floor of 9.8", math.floor(9.8))
print("Power of 8'2", pow(8,2))"""

#task
#create a function take random value using random Module
#check if the value is positive or negative and print it 
#check if the value is divisible with 5 or not and print it
#check if the value is odd or even

"""import random

def num():
    x= random.randint(-10,10)
    print("random no. is :",x)
    if x >= 0:
        print("number is positive")
    else:
        print("number is negative")

    if x % 5 == 0:
        print("number is divisible by 5")b
    else:
        print("number is not divisible by 5")

    if x % 2 ==  0:
        print("number is even")
    else:
        print("number is odd")
num()"""

#Class : is an blueprint for creating objects
#Object : ia an instance of a class 

#calculator

"""class Calculator:
    def add(self,a,b):
        return a+b
calc=Calculator()
print(calc.add(5,3))"""

"""class abc:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = abc("Yash", 18)
print(p1.name,p1.age)"""
#print(p1.age)

# class Person:
#     x=5
# a = Person()
# print(a.x)  

"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"My name is {self.name} and I am {self.age} years old")
result=Person("Yash",18) 
result.greet()"""       

#make a calculator using class

"""class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero!"
        return a / b

    @staticmethod
    def main():
        calc = Calculator()
        while True:
            print("\nOperations:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '5':
                print("Exiting Calculator. Goodbye!")
                break

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", calc.add(num1, num2))
            elif choice == '2':
                print("Result:", calc.subtract(num1, num2))
            elif choice == '3':
                print("Result:", calc.multiply(num1, num2))
            elif choice == '4':
                print("Result:", calc.divide(num1, num2))
            else:
                print("Invalid choice! Please select a valid operation.")


# Run program
Calculator.main()"""


#create class named as rectangle
#there is attributes in it length and width
#these is method named as area which return area of rectangle
#Get input from user for a and b
#hint:

#area=lenght*breadth
#return area

#l=float(input("Enter lenght:"))
#w=float(input("Enter width:"))

#area=Rectangle(l,w)

"""class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

l = float(input("Enter length: "))
w = float(input("Enter width: "))

rect = Rectangle(l, w)

print("Area of Rectangle:", rect.area())"""

#class

"""class Car:
    def __init__(self,brand,color):
        self.brand=brand #attribute
        self.color=color #attribute

    def drive(self): #method
        print(f"{self.color} {self.brand} is driving 🚗")"""

#object
"""car1= Car("BMW","Blue")
car2= Car("Defender","Black")

car1.drive()
car2.drive()"""

#Encapsulation --> binding data + methods together

#bankaccount

"""class BankAccount:
    def __init__(self,balance):
        self.__balance += balance

    def deposit(self,amount):
        self.__amount +=amount

    def get_balance(self):
        return self.__balance 

account = BankAccount(1000)
account.deposit(500)
print(account.get__balance()) #1500"""

#inheritance

#class car (private)

"""class car:
    def __init__(self,brand,color):
        self.brand=brand #attribute
        self.__color=color #attribute

    def drive(self): #mentioned
        print(f"{self.__color} {self.brand}is driving 🚗")
#object
car1=car("bmw","black")
car2=car("tesla","white")

print(car1.brand)
print(car1.__color)
print(car2.brand)
print(car2.__color)

car1.drive()
car2.drive()"""

#polymorphism

#class animal speak

"""class animal:
    def speak(self):
        print("animal speaks")
class Dog(animal):
    def speak(self):
        print("dog barks🐶")
dog=Dog()
dog.speak()"""    

#class animal sound

"""class Cat:
    def sound(self):
        return "Meow 🐱"
class Dog:
    def sound(self):
        return "Woof 🐶"

for animal in [Cat(),Dog()]:
    print(animal.sound())"""   
 
"""class Animal:
    def speak(self):
        print("Animal make different sound")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
class Cat(Animal):
    def speak(self):
        print("Cat meows")
for pet in (Dog(),Cat()):
    pet.speak()"""                        

#Abstraction

"""from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(vehicle):
    def start(self):
        print("Car started")

class Bike(vehicle):
    def start(self):
        print("Bike started")

vehicles = [Car(),Bike()]

for v in vehicles:
    v.start()"""



#PANDAS

#pip install pandas
#or
#python -m pip install pandas
#pip --version

"""import pandas as pd

data=[10,20,30,40]
s=pd.Series(data)

print(s)"""

"""import pandas as pd

data = {
    'name' : ['virat','ayush','nitesh','yash'],
    'age' : [21,23,18,12],
    'marks' : [91,90,89,88]
}

df= pd.DataFrame(data)
print(df)
print(pd.__version__)"""

"""import pandas as pd

Data = [34,67,45]
y=pd.Series(Data)
print(y)"""

#series

"""import pandas as pd
a=[1,7,2]
#myvar = pd.Series(a)
myvar = pd.Series(a, index=['x','y','z'])
print(myvar["y"])
print(myvar)"""

"""import pandas as pd
calories={"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)"""

"""import pandas as pd

df = pd.read_csv("crocodile_dataset.csv")
print(df.head())
print(df.tail())
print(df.info())"""


#Q1 Create a pndas series from a dictionary:
# {"math":90,"science":85,"english":78}
# print the series
# access the marks for science
# show its .dtype amd .shape

"""import pandas as pd
marks={"math":89,"science":45,"sst":67}
e=pd.Series(marks)
print(e)
print(e[1])"""

#Q2create a series with numbers [5,10,15,20,25]
# add 5 to each element
# multiply the series by 2
# print the first 3 elements using slicing