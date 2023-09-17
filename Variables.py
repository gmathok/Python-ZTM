# Variables and Best Practices
# Green Mathok
# 9/17/2023

# Variable names should be descriptive
# IQ is a variable holding the value 190
iq = 190
print(iq)

# Use meaningful variable names; avoid overly cryptic or single-letter names
# Using snake_case for variable names makes them more readable
_user_iq = 190  # Variable names can start with a letter or underscore
print(_user_iq)

# Variable names are case-sensitive; 'user-iq' is different from 'user_Iq'
user_iq = 190
print(user_iq) #if this was user_Iq then it would result in an error

# Avoid reassigning built-in names like 'print'
# print = 190  # This will result in an error

# Unique variable names are easier to distinguish from keywords
wasxd = 190 # unique variable
def # This is a keyword

##################################

# Reassigning variables and performing calculations
iq = 190
user_age = iq / 4
print(user_age)

# Variables can be reassigned to other variables
a = user_age
print(a)

# Constants (Values that never change in a program)
PI = 3.14
# PI = 0  # Although you can reassign constants, it's a convention not to change them

# Dunder Variables (Double Underscore Variables used by Python)
# Avoid creating variables with double underscores, as they have special meanings in Python
# __hihi = "hi"

##################################

# Rapidly assign values to multiple variables in a single line
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
