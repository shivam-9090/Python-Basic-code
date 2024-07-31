# -> OOP in python :

# -> oop means object oriented programming.

# -> this is upgrade level of function.

# -> Class & object in python:

# -> Creating object

# -> class Student :   (but always name first letter is capital)
        # -> write something

# -> creating object(instance)
# -> s1 = Student()
# -> print(s1.name)




# ->  __init__Function
# -> constructors :
# -> All classes have a functins called __init__(),which is always executed when the class is being intiated



# -> Class & Instance Attributes :

# -> class.attr
# -> obj.attr



# -> Static methods :

# -> methods that don't use the self parameter (work at class level)

# -> Syntax :
class Student:
       @staticmethod  #decorator
       def collage():
        print("my collage")



# -> IMP :

# -> 1) Abstraction :


# -> -> Hiding the implemention details of a class and only showing the essenial feature to the user.
# -> -> matlab unnecessary file hide karvani rit athva je kamnu hoy ej batavu bakinu hide karavu.
 
# Example code :
class Car :
    def __init__(self) -> None:
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self) :
        self.clutch = True
        self.acc = True
        print('car strted..')


car1 = Car()
car1.start()



# -> 2) Encapsulation :

# Wrapping data and functions into a single unit(onject).
# function and data nu comibination etle encapsulation

# -> Example code :
class Account() :
    def __init__(self, bal, acc) -> None:
        self.balance = bal
        self.account_no = acc


    def debit(self, amount) :
        self.balance -= amount
        print("Rs.",amount, "was debited")
        print("total balance = ", self.get_balance())

    def credit(self, amount) :
        self.balance += amount
        print("Rs.",amount, "was credited")
        print('Total baalance = ', self.get_balance())

    def get_balance(self):
        return self.balance

acc1 =Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(49400)
acc1.debit(200)


# complete lecture 8 and youtube link : https://youtu.be/HeW-D6KpDwY?si=MS_4NTTStBkprtRn