#Define Simple Dictionary
# person = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# #Accessing values in the dictionary
# print(person)
# print("Name", person["name"])#Alice
# print("Age", person["age"])# 30
# print("City", person.get("city"))# New York
# print("City", person.get("city"))   #New york

# for key,value in person.items():
#     print(f"{key}: {value}")#Name: Alice, Age: 30, City: New York

# #Adding a new key-value pair
# person["Job"] = "Engineer"
# print("updated person dictionary:", person)

# #Updtating on eisting key
# person["age"] = 31
# person["city"] = "Los Angeles"
# print("Updated person dictionary:", person)

# #Deleting a key value pair
# del person["Job"]
# print("Person dictionary after deleting Job:", person)

# #Checking if a key exists
# if "name" in person:
#     print("Name exists in the dictionary")

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"d": 4, "e": 5}
# #Merging two dictionaries
# dict1.update(dict2)
# print("Merged dictionary:", dict1)

#Nested dictionary
student = {
    "person1": {
        "name": "Alice",
        "age": 30
    },
    "person2": {
        "name": "Bob",
        "age": 25
    },
    "person3": {
        "name": "Charlie",
        "age": 35
    },
    "person4": {
        "name": "David",
        "age": 28
    },
    "person5": {
        "name": "Eve",
        "age": 22
    }
}
