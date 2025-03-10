class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return "The car is started!"


class BankAccount:
    def __init__(self, acc_num):
        self.__acc_num = acc_num
        self.__balance = 0
    
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
        else:
            print("Insufficient Funds")
    
    def check_balance(self):
        return self.__balance
    

# base class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id

    def __str__(self):
        return "Overridden successfully"

class Address:
    def __init__(self, street, city, code):
        self.street = street
        self.city = city
        self.zip_code = code
    
class Person1:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count
import math
class MathOperations:
    @staticmethod
    def sqrt(x):
        return math.sqrt(x)

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__length
    
    def set_length(self, length):
        self.__length = length

    def get_width(self):
        return self.__width
    
    def set_width(self, width):
        self.__width = width

rect = Rectangle(10,5)

# print(rect.get_length(), rect.get_width())


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"{math.pi*self.radius*self.radius}"
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return f"{2*self.length*self.width}"
    

# operator overloading

class Imaginary():
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary
    
    def __str__(self):
        return (f"Complex({self.real}, {self.imag})")

    def __add__(self, other):
        return Imaginary(self.real + other.real, self.imag + other.imag)
    
    def __subt__(self, other):
        return Imaginary(self.real - other.real, self.imag - other.imag)
    
    def __mult__(self, other):
        return Imaginary(self.real * other.real, self.imag * other.imag)
    
    def __add__(self, other):
        return Imaginary(self.real + other.real, self.imag + other.imag)
    

# imag = Imaginary(2,3)
# imag1 = Imaginary(1,5)
# print(imag + imag1)

# print(dir(imag))

def max_consecutive_difference(lst):
    max_diff = 0
    for i in range(1, len(lst)):
        a = lst[i] - lst[i-1]
        if a < 0:
            a *= -1
        if a > max_diff:
            max_diff = a
    return max_diff

# lst = [10, 11, 15, 3]
# print(max_consecutive_difference(lst))

list1 = [1, 4, 7]
list2 = [2, 3, 5, 8]

for i in range(len(list1)):
    for j in range(len(list2)):
        if list2[j] > list1[i] and list2[j] < list1[i+1]:
            list1.insert(i+1,list2[j])
print(list1)