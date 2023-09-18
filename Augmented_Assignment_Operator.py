#This code demonstrates the proper usage of the augmented assignment operator and
#that the operator has to be left of the equal sign.

#  Code without Augmented assignment operator 
# some_value = 5
# some_value = some_value + 2

# print(some_value)

########################################################
#Usage of Augmented assignment operator
# some_value = 5
# some_value  += 2
# print(some_value)

##########################################################
# some_value -=5
# print(some_value) #will result in a name error due to the
# variable some_value not being declared.

##########################################################
# Augmented assignement with multiplication operator
# some_value = 5
# some_value *= 2
# print(some_value)

########################################################
# augmented assignment with division operator
some_value = 5
some_value /= 2
print(some_value)
