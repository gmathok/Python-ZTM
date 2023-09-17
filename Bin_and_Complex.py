# Bin function used to return binary representation of integer as a string
print(bin(5))  #0b101  python inludes b to indicate a binary number 101
print(int('0b101', 2))  # number is base 2 & convert to integer

# Convert an integer to binary representation
decimal_number = 10
binary_representation = bin(decimal_number)
print(binary_representation) # Output: '0b1010'

############################################################

# complex (complex numbers, represented using 'j' suffix for the imaginary part.)
# Creation
z1 = 2 + 3j
z2 = 1 - 2j

#Addition of complex numbers
result_add = z1 + z2
print(result_add) # Output: (3+1j)

#Subtraction of complex numbers
result_sub = z1 - z2
print(result_sub) # Output: (1+5j)

# Multiplication of complex numbers
result_mul = z1 * z2
print(result_mul) # Output: (8+1j)

# Division of complex numbers
result_div = z1 / z2
print(result_div) # Output: (-0.8+1.4j)
