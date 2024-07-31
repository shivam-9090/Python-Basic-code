a = 5 // 2 #integer
b = 5 / 2  #float

print(a)
print(b)

# Output:
# 2
# 2.5

# TRY, EXCEPT, ELSE, FINALLY Program :
try:
    # code that might raise an exception
    result = 1 / 0      # result = 1/1
except ZeroDivisionError:
    # code to handle the exception means that result is not acceptable.
    print("Cannot divide by zero")
except Exception as e:
    # code to handle any other exception means that result is error.
    print("An error occurred:", str(e))
else:
    # code to run if no exception occurred means that result is acceptable.
    print("No exception occurred")
finally:
    # code to run regardless of whether an exception occurred or not mean that always run.
    print("This code will always run")

# swapcase use for upper to lower and lower to upper.
string = 'shivam'
print(string.swapcase()) #SHIVAM

# return docstring of function or class means like return string.

class Svm() :
    def __doc__(self) :
        return print("This is a SVM model")

s1 = Svm()
s1.__doc__()



# math module in python
# floor function use:
import math
number = 3.7

# Round down to the nearest integer
rounded_number = math.floor(number)  #floor() like maths subject box[3.7] = 3

print(rounded_number)



# Dictonary comprehension is like that :  (comprehension means is samaj.)
my_dict = {i:i+7 for i in range(1, 10)}

print(my_dict) #output : {1: 8, 2: 9, 3: 10, 4: 11, 5: 12, 6: 13, 7: 14, 8: 15, 9: 16}



# Differentiate between List and Tuple?

# List

# -> Lists are Mutable datatype.
# ->Lists consume more memory
# ->The list is better for performing operations, such as insertion and deletion.
# ->The implication of iterations(journey) is Time-consuming

# Tuple

# ->Tuples are Immutable datatype.
# ->Tuple consumes less memory as compared to the list
# ->A Tuple data type is appropriate for accessing the elements
# ->The implication of iterations is comparatively Faster



# use of iterator in python :

my_list = [1, 2, 3, 4, 5]

# Create an iterator from the list
iterator = iter(my_list)

# Iterate over the iterator
for element in iterator:
    print(element)       # 1, 2, 3, 4, 5(separated)


