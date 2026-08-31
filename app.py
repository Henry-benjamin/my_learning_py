##1 VARIABLE

price = 10 #integer number
rating = 4.8 # float number
name = "Henry" # string
is_published = True #boolean
#print(price) # print is for output.

##2 INPUT FUNCTION AND OUTPUT FUNCTION
#name = input("what is your name? ") #input gets the inform form a user
#favorite_color = input("what is your favorite color? ")
#print(name + " likes " + favorite_color)

#3 TYPE CONVERSION
#input always return a string
# str() convert a number into a string
#int() is to convert a string into an integer number(10)
#float() convert a str into a float number(1.6)
#type is to checks the type of variable

#birth_year = input("Birth year: ") 
#print(type(birth_year))
#age = 2026 - int(birth_year)
#print(type(age))
#print(age)

#weight_lbs = input("Weight (lbs): ")
#weight_kg = int(weight_lbs) * 0.45
#print("your kilogram is:", + weight_kg)

##4 STRING
course = "python for 'Beginners'"
#print(course)
tree_quotes = """
This treepli quotes is for 
log sentences like this.
"""
#print(tree_quotes)

#how to access index of string 
course = 'Python for Beginners'
#print(course[0]) # get the firts letter(P)
#print(course[-1]) # get the last one(s)
#print(course[0:3]) # return all the charaters foem zero to 3(pyt)
#print(course[1:])# remove just first letter and return rest of them
#print(course[:])# this copy the string it means the copy of the string

#FORMATTED STRINGS
first = 'Henry'
last = 'benja'
message = f"{first} {last} is a coder"
#print(message) 

#STRING METHODS
cour = "Python is cool language"
len(cour)# is a method to calculate the number of charaters in a string
cour.upper()#this turn the whole string into the upperCase
cour.lower()#this turns into lowercase
cour.find('p')#find the index of character in a string
cour.replace('Python', 'JavaScript') # is to replace a string with another string takes two arguments

'python' in cour # this give us a boolean Trou or False is to check if the sting exists in a particular string

#5 ARITHMETIC OPERATIONS
#the operations signs are + - * /
x = 10
x += 3 # is equal to x = x + 3

#operator Precedence
x = 10 + 3 * 2 # 16
#these are the priorite of calculation
#parenthesis
#exponentiation 2 ** 3
#multiplication or division
#addition or substraction

#Math Functions 
x = 2.9
round(x)# it rounds to the nearest integer(3)
abs(-2.9)# always returns a positive number not matter what 
import math # to perform well math we import math then use all its functions

#6 IF STATEMENTS
is_hot = False
is_cold = False

#if is_hot:
    #print("It's a hot day")
    #print("Drink plenty of water")
#elif is_cold:
    #print("It's cold day")
    #print("Wear warm clothers")
#else:
    #print("It's a lovely day")
#print("Enjoy your day")

#CHALLANGE
price = 100000
has_good_credit = True

if has_good_credit:
    down_payment = price * 0.1
else :
    down_payment = price * 0.2
#print(f"Down payment: ${down_payment}")