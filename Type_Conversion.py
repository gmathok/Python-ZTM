# This program demonstrates the use of the type function.
str(100) #converts the integer value 100 to a string

#convert 100 into a string, check the type and print it out
# print(type(str(100)))

##########################################################
#convert 100 into a string,then back into integer, check the type & print it out
# print(type(int(str(100))))

# equivalent but longer code without the usage of type function
a = str(100)
b = int(a)
c = type(b)
print(c)
