# Fundamental Data Types
# int
# float
# bool
# list
# tuple
# set
# dict

# Classes -> Custom types

# Specialized Data Types (used from modules)
# None (absence of value)

###################################################
# Green Mathok
##################################################

# Identity function (int and float)
print("Identity function results:")
print(type(2 + 4))  # Addition
print(type(2 - 4))  # Subtraction
print(type(2 * 4))  # Multiplication
print(type(2 / 4))  # Division
print(type(2.1 + 4.9))  # Float addition
print(type(2 ** 4))  # Exponentiation
print(type(10 // 4))  # Integer division
print(type(10 % 4))  # Modulo

# Math functions (round and absolute value)
print("\nMath functions results:")
result1 = round(3.1)
print("Rounded 3.1:", result1)
result2 = abs(-20)
print("Absolute value of -20:", result2)

# Additional math functions
import math

print("\nAdditional math functions:")
print("Square root of 16:", math.sqrt(16))
print("Ceiling of 3.7:", math.ceil(3.7))
print("Floor of 3.7:", math.floor(3.7))
print("Sin of 45 degrees:", math.sin(math.radians(45)))
print("Cos of 45 degrees:", math.cos(math.radians(45)))