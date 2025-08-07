# Tuple
_tuple1 = ()#Creating an empty tuple
_tuple1 = (1, 2, 3)  # Creating a tuple with three elements
_tuple1 = ("Vorrawat", "Vettayavong", 17)  # Tuple with multiple elements

# Accessing items in a tuple
print("Tuple: ", _tuple1)
print("First item: ", _tuple1[0])
print("Second item: ", _tuple1[1])

print("Length of tuple: ", len(_tuple1))

#slicing the tuple
print("Sliced tuple (1:3): ", _tuple1[1:3])  

# _tuple = ("Vorrawat", "Vettayavong", 17) 
#Adding items to a tuple
#Chanaing items in a tuple is not allowed, but you can create a new tuple with the desired changes
#Deleting items from a tuple is also not allowed
_tuple1 =list(_tuple1)  # Converting tuple to list
_tuple1.append(20)
_tuple1.insert(1, "NewItem")  # Inserting an item at index 1
_tuple1[0] = "UpdatedItem"  # Updating the first item

_tuple1 = tuple(_tuple1)  # Converting list back to tuple
print("Tuple after adding and changigng items: ", _tuple1) 


