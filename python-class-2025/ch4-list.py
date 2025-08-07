# # #list
# # _list =[]#list to store items
# # _list= [1, 2, 3, 4, 5] #initializing list with some values
# # _list2 =["a",20.0,30,"b",40] # list with mixed data types
# # student = ["6807012660017", "Vorrawat", "Vettayavong","namo.v06@gmail.com",17] # list with student details

# # print("Student: ",student)
# # print("Student ID: ",student[0])
# # print("Student Name: ",student[1],student[2])
# # print("Student Email: ",student[3])
# # print("lenght of student : ",len(student))

# # print(student[1:3]) # slicing list to get name

# adding items to list
# _list1 = [1, 2, 3, 4, 5]#Initializing list with some values
# _list1.append(10) #adding item to the end of the list
# print("List after appending 10: ", _list1)
# _list1.insert(2,5)#iserting an item at the beginning of the list
# print("List after inserting 5 at index 2: ", _list1)

# #[1, 2, 3, 4, 5, 10
# #Removing items from list
# _list1.remove(3) #removing item from the list]
# print("List after removing 3: ", _list1) # [1, 2, 4, 5, 10]
# _list1.pop() #removing last item from the list
# print("List after popping last item: ", _list1)

# #Editing items in list
# _list1[0] = 100 #editing first item in the list
# _list1[1] = 200 #editing second item in the list
# print("List after editing first two items: ", _list1) # [100, 200, 4, 5]=

# #Multiple items in list
# _list2 =[6,7,9]#list with mixed data types
# _list1.extend(_list2) #adding multiple items to the list
# print("List after extending with _list2: ", _list1) # [100, 200, 4, 5, 6, 7, 9]

# #sorting list
# _list1.sort() #sorting list in ascending order
# print("List after sorting: ", _list1) # [4, 5, 6, 7, 9, 100, 200]
# #Reverse sorting
# _list1.reverse() #sorting list in descending order
# print("List after reversing: ", _list1) # [200, 100, 9, 7, 6, 5, 4]

# #Copying the list
# a = 3
# b = a
# _list3 =_list1
# print("list 1: ", _list1)#[200, 100, 9, 7, 6, 5, 4
# print("list 3: ", _list3)#[200, 100, 9, 7, 6, 5, 4
# _list3[0] = 1000 #editing first item in the list
# print("list 1 after editing list 3: ", _list1)#[1000, 100, 9, 7, 6, 5, 4]

# _list3 = _list1.copy() #copying the list
# _list3[0] = 1000 #editing first item in the list
# print("list 1 after copying and editing list 3: ", _list1)  # [200, 100, 9, 7, 6, 5, 4]
# print("list 3 : ", _list3)  # [1000, 100, 9, 7, 6, 5, 4]

# #clearing the list
# _list3.clear() #clearing the list
# print("List after clering: ",_list3)  # []

# #Deleting the list
# del _list1  #deleting the list

# print("List 3 after delation: ", _list3)  # Raises NameError as _list3 is cleared and deleted

#Checking if an item exists in the list
# if 100 in _list1:
#     print("100 is in the list")
# else:
#     print("100 is not in the list")

# #Iterating through the list
# for item in _list1:
#     print("Item:", item)

# for index in range(len(_list1)):
#     print("Item at index", index, ":", _list1[index])
    
