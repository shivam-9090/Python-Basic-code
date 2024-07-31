# Del keyword :

# -> use to delete object properties or object itself.

#  -> Example code :
class Student():
    def __init__(self,name) -> None:
        self.name = name

s1 = Student('shivam')
print(s1.name)
del s1 #there is name is delete and name is not declare in output.


# Privet(Like) attribute & ,methods

#  -> Example code :
class Account() :

    def __init__(self,acc_no,acc_pass) -> None:
        self.acc_no = acc_no
        self.acc_pass = acc_pass

acc1 = Account(102325,456789)
print(acc1.acc_no)
print(acc1.acc_pass)

# -> output : 102335 and 456789

# -> but we try like this simple change in code:

class Account() :

    def __init__(self,acc_no,acc_pass) -> None:
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  #in this line i have change (__acc_pass) simple two line private our data 

acc1 = Account(102325,456789)
print(acc1.acc_no)
print(acc1.acc_pass)

# -> output : 102325 and error


# 3)  Inheritance :

# when one class drives the properties & methods of another class.
# Example: parent/child


# -> Types :
# 1) single inheritance

# -> Example code :
class Car :
    @staticmethod
    def start():
        print('car started..')

    @staticmethod
    def stop():
        print('car stopeed..')

class Toyotacar(Car):
    def __init__(self, name) -> None:
        self.name = name

car1 = Toyotacar('fortuner')
print(car1.start())


# 2) multi-level inheritance

#  -> Example code:
class Car :
    @staticmethod
    def start():
        print('car started..')

    @staticmethod
    def stop():
        print('car stopeed..')

class Toyotacar(Car):
    def __init__(self, brand) -> None:
        self.name = brand

class Fortuner(Toyotacar) :
    def __init__(self, type) -> None:
        self.type = type

car1 = Fortuner('diesel')
car1.start()


# 3) multiple inheritance

# -> Example code:
class A:
    varA ="welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):  #Multiple class use
    varc = "welcome to class C"

c1 = C()
print(c1.varA)

print(c1.varB)



# Super method :

# super() method is used to access methods of the parent class.

# -> Example code :
class Car :

    def __init__(self, type) -> None:
        self.type = type


    @staticmethod
    def start():
        print('car started..')

    @staticmethod
    def stop():
        print('car stopeed..')

class Toyotacar(Car):
    def __init__(self, brand, type) -> None:
        self.name = brand
        super().__init__(type)  #Super method
        

car1 = Toyotacar('parius','petoral')
print(car1.type)



# Class method :

# -> a class method is bound to the class & receives the class as an implict first argument.

# -> Note = static method can't access or modify class state & generally for utility.

# -> Example code:
class Person:
    name = 'shivam'

    @classmethod      #This is change direct class argument.
    def changename(cls, name):
        cls.name = name

p1 = Person()
p1.changename('shivam kumar')
print(p1.name)
print(Person.name)



# Property :

# We use @property decorator on any method in the class to use method as a property.

# -> Example code :
class Student:
    def __init__(self, phy, chem, math) -> None:
        self.phy = phy
        self.chem = chem
        self.math = math

    # def calculate(self):
    #     self.percentage = str((self.phy + self.chem + self.math ) / 3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math ) / 3) + "%"

stu1 = Student(93,76,90)
print(stu1.percentage)

stu1.phy =89
print(stu1.percentage)



# 4) Polymorphism : Opertor Overloading

# When the same operator is allowed to have different meaning according to the context.

# -> Example code:
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real,"i +", self.img, "j")

    def __add__(self, num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newreal, newimg)
    
    def __sub__(self, num2):
        newreal = self.real - num2.real
        newimg = self.img - num2.img
        return Complex(newreal, newimg)

num1 = Complex(1, 3)
num1.shownumber()

num2 = Complex(2, 4)
num2.shownumber()

num3 = num1 + num2
num3.shownumber()

num4 = num1 - num2
num4.shownumber()

# complete lecture 9 and youtube link : https://youtu.be/bAwmZVJeO5s?si=HS3aHPKw6DjVwX9q