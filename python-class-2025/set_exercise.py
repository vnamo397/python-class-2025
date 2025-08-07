fruits = {"apple","banana","cherry"}
more_fruits = {"orange", "mango","grape"}

print("Apple is present?", "apple" in fruits)

fruits.add("orange")  # Adding an item
print("Fruits after adding orange:", fruits)
print("Fruits after adding more fruits:", fruits.union(set(more_fruits)))

fruits.update(more_fruits)  # Adding multiple items
print("Fruits after updating with more fruits:", fruits)

#Removing an item
fruits.remove("banana")  # Raises KeyError if item not found
print("Fruits after removing banana:", fruits)
