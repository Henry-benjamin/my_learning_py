##1 VARIABLE

price = 10 #integer number
rating = 4.8 # float number
name = "Henry" # string
is_published = True #boolean
#print(price) # print is for output.

##2 INPUT FUNCTION AND OUTPUT FUNCTION
name = input("what is your name? ") #input gets the inform form a user
favorite_color = input("what is your favorite color? ")
#print(name + " likes " + favorite_color)

#3 TYPE CONVERSION
#input always return a string
# str() convert a number into a string
#int() is to convert a string into an integer number(10)
#float() convert a str into a float number(1.6)
#type is to checks the type of variable

birth_year = input("Birth year: ") 
#print(type(birth_year))
age = 2026 - int(birth_year)
#print(type(age))
#print(age)

weight_lbs = input("Weight (lbs): ")
weight_kg = int(weight_lbs) * 0.45
#print("your kilogram is:", + weight_kg)

##4 STRING
course = "python for 'Beginners'"
#print(course)
tree_quotes = """
This treepli quotes is for 
log sentences like this.
"""
#print(tree_quotes)
