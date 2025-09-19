# String is immutable

str1 = "Aryan chaudhary"
str2 = "Ayush Chaudhary"
str3 = "This is a string \n we are creating it in Python"

print(str3)

# operations

# concatenations
str = str1 + " " + str2
print(str)

# length
length = len(str)
print(length);

# indexing
ch = str[0]
print(ch)

#slicing
print(str[0:5])

print(str[:5])
print(str[0:])

# we can also do it - indexing
print(str[-3:-1])


# functions

# endswith
str = "I am studying python from ApnaCollege"
print(str.endswith("app"))

# capitalize
print(str.capitalize()) # make new string and then capatilize

# replace
print(str.replace("I", "hey"))

# find
print(str.find("python"))

# count
print(str.count("a"))

