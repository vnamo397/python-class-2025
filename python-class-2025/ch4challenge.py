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

#Output each person name and age
for i in range(1,6):
    person = student[f"person{i}"]
    print(f"person {i} {person['name']},{person['age']}")