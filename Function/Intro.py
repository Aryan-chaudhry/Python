# function to find length of list

def getLength(lst):
    length = len(lst)
    return length

# function to print the element of list in same line

def printElement(lst):
    for el in lst:
        print(el, end=" ")

list = ["Aryan", "Ayush", "Muskan"]
length = getLength(list)
print(length)

printElement(list)

