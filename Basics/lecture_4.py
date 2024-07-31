# Dictionary in python :

# dictionary are used to store data values in key:value pairs
# they are unordered,mutable(changeble) & don't allow duplicate keys

dict = {
    'name' : 'shivam',
    'key' : 'value',
    'lan' : 'python',
    'age' : 90,
    'is_adult' : True,
    'subjects' : ['python','c','javascript'],
    'topics' : ('dictionary','set'),
    'marks' : {     #this is nested dictionary
        'phy' : 97,
        'maths' : 98,
        'chem' : 96,
    }
}

print(type(dict))
print(dict)

dict['name'] = 'jagruti'
print(dict)

print(dict['marks']['chem'])


# Dict methods

print(dict.keys()) #returns all keys

print(dict.values()) #returns all values

print(dict.items()) #returns all (key, val) pairs as tuples

print(dict.get('key')) #returns the key according to value

dict.update({'city' : 'surat'})
print(dict)


# Sets in python :

# set is the collection of the unordered items
# each element in the set must be unique & immutable like tuple

num = {1,2,33,4,'shivam',4,2}

print(type(num))
print(num)

# num1 = {} empty dictionary
num1 = set() #empty set
print(type(num1))


# Set method
# set is mutable
# set values is immutable

num.add(5) #adds an element
print(num)

num.remove(5) #remove an element
print(num)

num.clear() #clear a set
print(num)

print(num.pop()) #clear values at random values


num2 = {5,6,9,7}
print(num.union(num2)) #combines both set values & returns new

print(num.intersection(num2)) #common values & return new


# complete lecture and on youtube link : https://youtu.be/078tYSD7K8E?si=STTUwiWk0oA8IW6g