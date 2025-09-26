# dict store key value pair, unordered, mutable, dont alloows duplicates keys

dict = {
    "Name" : "Aryan",
    "cgpa" : 7.5,
}

print(dict)

## Nested Dictionary

Profile = {
    "User_Name" : "Aryan_306",
    "createdAt" : {
        "Time" : "18:31",
        "Date" : "19-09-25"
    }
}

print(Profile)

# Method

# keys() --> return all keys
print(Profile.keys())

# values() --> return all values
print(Profile.values())

# items() --> return all (key,value) pair
print(Profile.items())

# get("Key")
print(Profile.get("User_Name"))

newProfile = {
    "user_name" : "itschaudharyAryan"
}

# update
Profile.update(newProfile)

print(Profile)
