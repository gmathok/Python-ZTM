# Demonstrating String Usage

# You can use single or double quotes to define strings
# print('hello Green')
# print("hello Green")

# Use the type() function to determine the data type of a string
# print(type("hello there Green!"))

# Collecting personal data like username and password
# username = "supercoder"
# password = 'supersecret'

# Using triple single quotes to create multiline strings (useful for long text)
# long_string = '''
# WOW
# -__-
# '''

# Concatenating strings using the + operator
# first_name = "Green"
# last_name = "Mathok"
# full_name = first_name + ' ' + last_name  # Adding a space for readability
# print(full_name)

# String interpolation (formatting) using f-strings (Python 3.6+)
# first_name = "Green"
# age = 36
# location = "Olathe"
# formatted_message = f"Hello, I am {first_name}. I am {age} years old and live in {location}."
# print(formatted_message)

# String slicing and indexing
message = "Hello, World!"
substring = message[7:12]  # Extracts "World"
print(substring)

# String length
string_length = len(message)  # Length of the string
print(string_length)

# Checking if a string contains a substring
contains_substring = "Hello" in message  # True
print(contains_substring)
