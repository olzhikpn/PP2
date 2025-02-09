#1.String Format

#You can not combine strings and numbers.

#Error Example
"""
age = 36
txt = "My name is John, I am " + age
print(txt)
"""

#2.F-Strings

#To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

#Example 1
age = 36
txt = f"My name is John, I am {age}"
print(txt) # My name is John, I am 36

#3.Placeholders and Modifiers

#A placeholder can contain variables, operations, functions, and modifiers to format the value.

#Example 1
price = 59
txt = f"The price is {price} dollars"
print(txt)

#A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

#Example 2
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Perform a math operation in the placeholder, and return the result:

#Example 3
txt = f"The price is {20 * 59} dollars"
print(txt)