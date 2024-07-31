# Strings :
# string is data type that stores a sequence of characters


print('hello '+'world') #Concatenation method

str1 = 'my name is shivam.\nmy age is 18.' #Use for new line \n
print(str1)


print(len(str1)) #Length of str

# Indexing :

str_a = 'shivam vaghani'
print(str_a[0])
print(str_a[1])
print(str_a[6])


# Slicing :

print(str_a[1 : 4])
print(str_a[ : ]) #start blank means zero and back end means at the last

print(str_a[-3 : -1]) #Spetial feature for python slicing



# String Function :

str3 = 'i am studying python from apnacollage'
print(str3.endswith('app')) #returns true if string end with substr

print(str3.capitalize()) #capitalize 1st char

print(str3.replace('am','was')) #replaces all occurrences of old char to new char

print(str3.find("python")) #returns 1st index of occurrer

print(str3.count('from')) #returns count occurrens of substance




# If-elif-else statments :
age = 18

if(age >= 18) :   # in that case if in or if there process called Nesting statement
    print('you are eligible for vote')
elif(age >= 30) :
    print('you are young for vote')
else :
    print('you are not eligible for vote')


#complete lecture 2 on youtube and link : https://youtu.be/lIId8IDP6TU?si=gvHqzir4IMpWHBU5