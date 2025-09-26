# List is mutable

List = [2, 3, 4, "Aryan", "Ayush", "Muskan"];
print(List);

print(List[1]);

List[3] = "Aryan Chaudhary";

print(List);

# functions

# append
List.append("A")

print(List);

# sort
#  only work if datatype of all element is same

List2 = [ "Muskan", "Aryan", "Ayush", "amarsingh"]
List2.sort()
print(List2);

# sort(reverse = True)  to sort in desending order work in same datatype
List2.sort(reverse=True)
print(List2);

# reverse
List2.reverse()

# insert
List2.insert(3, "Shanti")
print(List2)

# remove here we have key
List2.remove("Aryan")
print(List2)

# pop here we have index
List.pop(2)
print(List)
