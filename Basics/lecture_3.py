# List in python :

marks = [78,96,45.1,89,'shivam'] #this is list and write in []
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

# mutable means change list value
marks[4] = 'jagruti' #string are immutable and list are mutable
print(marks)


# List slicing :

print(marks[1 : 4])
print(marks[ : ])


# List method :

list = [2,1,3]

list.append(4) #adds one element at the end
print(list)

list.sort()  #sorts is assending order
print(list) 

list.sort(reverse = True)  #sorts is dessnding order
print(list) 

list.reverse()  #list reverse
print(list)

list.insert(1,6) #insert value in list
print(list)

list.remove(6) #remove first occurrance of element
print(list)

list.pop(2) #remove element at idx
print(list)



# Tuples in python

tup = (87,56,52,45) #this is tuple and written in () breket and tuple is immutable like string

print(tup[0])
print(type(tup))
# tup[0] = 85 this is error because tuple is immutable
# in tuple slicing is possible,you can use slicing in tuple


# Tuple method :

print(tup.index(56)) #returns index of first occurrance

print(tup.count(2)) #count total occurrance



# complete lecture 3 and on youtube and link : https://youtu.be/qVyvmzFxF_o?si=Z7YxQDHR4crl1kZw