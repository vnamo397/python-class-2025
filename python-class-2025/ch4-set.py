#set
#Empty set
empty_set = {}

#Int
my_set = {1, 2, 3,4,5}
#String
my_set = {"apple", "banana", "cherry"}

#Mixed data types
my_set = {1, "apple", 3.14,(1, 2)}

#Print sets
print("Empty set:", empty_set)

#list and tuple
my_set3 = {1,5,8,"AAA"}
my_set3 = list(my_set3)  # Convert set to list
my_set3[3] = "BBB"  # Edit the list

my_set3 = set(my_set3)  # Convert list back to tuple
print("Set with mix data types:", my_set3)


_list = {1, 2, 3, 4, 5}
_list = list(set(_list))  # Convert set to list
print("List after removing duplicates:", _list)

for item in my_set3:
    print(item)

# Adding items to a set
my_set3.add("CCC")
print("Set after adding 'CCC':", my_set3)

#Removing items from a set
my_set3.remove("BBB")  # Raises KeyError if item not found
print("Set after removing 'BBB':", my_set3)

#Checking meme=bership in a set
if "AAA" in my_set3:
    print("'AAA' is in the set")
else:
    print("'AAA' is not in the set")

#Clearing a set
my_set3.clear()  # Removes all items from the set
print("Set after clearing:", my_set3)

#Set operations
# Union
set_a = {1, 2, 3}
set_b = {3, 4, 5}

set_union = set_a|(set_b)
print("Union of set_a and set_b:", set_union)

# Intersection
set_intersection = set_a & set_b
print("Intersection of set_a and set_b:", set_intersection)

# Difference
set_difference = set_a - set_b
print("Difference of set_a and set_b:", set_difference)

# Symmetric Difference
set_symmetric_difference = set_a ^ set_b
print("Symmetric Difference of set_a and set_b:", set_symmetric_difference)
