'''
import keyword
print(keyword.kwlist)
Greet = "Hello world<---"

print(Greet)

#In python two type "comments" there to give Warning to devloper or reader 

#In-Line ----#
#Multiline --''''''
 

Text Type       : 	str
Numeric Types   : 	int, float, complex
Sequence Types  : 	list, tuple, range [1,"str",3,4] (1,"4.5",3,4) (start no, stop no, step no)
Mapping Type    : 	dict (key:value, location:India)
Set Types       : 	set, frozenset
Boolean Type    : 	bool (true or false)
Binary Types    : 	bytes, bytearray, memoryview
None Type       : 	NoneType

print("\n")
myVariableName = "John <<<<Camel Case"
print(myVariableName)

number = 4 + 6j

print(type(number))

print("\n")
Movie = "GOAT"
print(Movie)
print(len(Movie))
print("\n")
print(Movie[0],"In Index 0 in GOAT")
print(Movie[1],"In Index 1 in GOAT")
print(Movie[2],"In Index 2 in GOAT")
print(Movie[3],"In Index 3 in GOAT")
print("\n")

print(Movie[-1],"In Index -1 in GOAT")
print(Movie[-2],"In Index -2 in GOAT")
print(Movie[-3],"In Index -3 in GOAT")
print(Movie[-4],"In Index -4 in GOAT")

'''
#=========================Day2===========================

###################Type()-type###################

#Type used for to know the data type eg:str,int,tuple,etc..

# data = "5"
# print(type(data))

###################Len()-length###################

#Length is used for count the index in the data

# data = "John"
# print(len(data))

# print(data[0])
# print(data[3])

###########String Slicing : [start: end(n-1) :step]###########

# Slicing is used to strip the particular data from the data.
'''
ssl_validity="Not Before Tue, 14 May 2024 00:00:00 GMT Not After Fri, 06 Jun 2025 23:59:59 GMT"

print("Certificate valid from  ",ssl_validity[11:40])
print("Certificate Expire date is ",ssl_validity[51:])
'''

########## String concatenation ##############

#Example 1:
'''
ssl_validity="Not Before Tue, 14 May 2024 00:00:00 GMT Not After Fri, 06 Jun 2025 23:59:59 GMT"

start_date = ssl_validity[11:40]
end_date = ssl_validity[51:]

print("Certificate valid from",start_date,"and Certificate valid till", end_date)
print("\n")

#Example 2:

ssl_validity = start_date +" "+ end_date
d_type =type(ssl_validity)
print(ssl_validity,d_type,">>>>>>concatinantion using + sign")

print("\n")
ssl_validity1 = start_date
ssl_validity2 = end_date
ssl_validity = ssl_validity1,ssl_validity2
d_type =type(ssl_validity)
print(ssl_validity,d_type,">>>>>>concatinantion using , sign")
'''

###################String Modification#############

"""
    - lower() -> Lowercase
    - upper() -> Uppercase
    - strip() -> Remove White Space
    - replace() -> Replace a String
    - split()  -> Split a String

"""
'''
data = "Python is awsome"

print(data, "<<<<< Orignal Version") 

user_input = input("Please shop by serch eg:apple, Laptop,Vegitable: ")
print(user_input.lower(),"<<<<<LowerCase")
print(user_input.upper(),"<<<UpperCase")
'''
'''
#################strip()####################

#The strip() method removes any leading, and trailing whitespaces
space = "Apple vegi"
space1 = "  Apple vegi  "
print(len(space), "Cleand extra space mannully")
print(len(space1), " not cleaned")
print("\n")
#space1 = space1.strip()
space1 = space1.lstrip()
space1 = space1.rstrip()
print(len(space1))
'''
'''
#################replace()####################

raw = "welcome to the python summar class,summarsummarsummarsummarsummar"

print(raw)

raw = raw.replace("summar","winter")

print(raw)
'''
#################split()####################

'''
raw = "Hello;world!, Welcome; to the python"

raw = raw.split(";")

print(raw[-1])
'''

########### Format - String ############

Name = "Johny Boy"
age = 18

'''
print(Name,age, "First Method")
print("\n")
print("Hi", Name,"your age is",age,"Second Method")
print("\n")
data = "Hi {Name} your age is {age}"
data = data.format(Name,age)
print(data)
print('Hi {0} your age is {1}'.format(Name,age), " Using Index")
print('Hello {a} you are {b}'.format(a = Name, b = age), " Using additional variable")
'''
###############F-String###################
'''
print(f'Hello {Name} you are {age}')
'''
######Boolean Type : bool()#######
"""
    True
    False
True Values in Python :

    any string is true - Except empty string
    any number is true - except 0
    any list ,tuple,set,dict - except empty
"""    
'''
with_string = "Data"
empty_string = ""

print(bool(with_string))
print(bool(empty_string))
print("\n")

with_number = 1
empty_number = 0

print(bool(with_number))
print(bool(empty_number))

print("\n")

ls = ["a",1]
empty_ls = []
print(bool(ls))
print(bool(empty_ls))
'''


#Operators :

"""
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators

"""

# Arithmetic Operators :

"""
Addition       =>  +
Subtraction    =>  -
Multiplication =>  *
Division        =>  /
Floor Division   =>  //
Modulus          =>  %
Exponentiation   =>  **
"""

a,b =2,4

# Addition
Total = a+b
print(f"Addition: The sum of a + b : {Total}" )
print("\n")
# Subtraction
Total = a-b
print(f"Subtraction: The sum of a - b : {Total}" )
print("\n")
# Multiplication
Total = a*b
print(f"Multiplication: The sum of a * b : {Total}" )
print("\n")
# Division
Total = a/b
print(f"Division: The sum of a / b : {Total}" )
print("\n")
# Floor Division
Total = a//b
print(f"Floor Division: The sum of a // b : {Total}" )
print("\n")
# Modulus
Total = a%b
print(f"Modulus: The sum of a % b : {Total}" )
print("\n")
# Exponentiation
Total = a**b
print(f"Exponentiation: The sum of a ** b : {Total}" )
print("\n")


############ Comparison operator ###########

"""
    ==   =>  equal 
    !=   =>  Not equal
    >    =>  Greater than
    <    =>  Less than 
    >=   =>  Greater than or equal to
    <=   =>  Less than or equal to


a,b = 3,6
print(f'')
# equal
print(f'{a==b}, the value\'s of a:{a} and b:{b} is not equal')
print("\n")
print(a!=b)
print("\n")
print(a>b)
print(a<b)
print("\n")
print(a>=b)
print(a<=b)

"""
############ Logical Operator ##############
"""
    and
    or
    not
"""
a,b = 3,6

print(a>1 and b>a)
print(a>1 or b>a)
print(a>1 and not b>a)



######## Identity Operator ############

