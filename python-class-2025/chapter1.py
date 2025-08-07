# # # # # # # Variables and Data Types
# # # # # # a = 5       # integer
# # # # # # b = 5.0     # float
# # # # # # c = "Vorrawat Vettayavong" # String
# # # # # # d = True    # Boolean True or False
# # # # # # e = 6+5j    # Complex

# # # # # # print(a)
# # # # # # print(b)
# # # # # # print(c)
# # # # # # print(d)
# # # # # # print(e)

# # # # # # a = 55
# # # # # # b = 6.5
# # # # # # print(a)
# # # # # # print(b)

# # # # # # z = a+b # float
# # # # # # print(z)

# # # # # # #Descriptive name or meaning full name
# # # # # # tax = 0.07
# # # # # # firstname = "Vorrawat"
# # # # # # email = 'namo.v06@gmail.com'
# # # # # # age = 17

# # # # # # # Multi words variable name
# # # # # # # Snake case
# # # # # # student_first_name ='Vorrawat'
# # # # # # student_last_name ='Vettayavong'
# # # # # # student_age = 17
# # # # # # student_email = "namo.v06@gmail.com"

# # # # # # print("Student name:" + student_first_name)
# # # # # # print(f"Student lastname: {student_last_name}")

# # # # # # Data Types
# # # # # a = 1       #int
# # # # # b = 1.1     #float
# # # # # c = '1'     #string

# # # # # print(a+a)  # 2
# # # # # print(b+b)  #2.2
# # # # # print(c+c)  #11
# # # # # print(a+b)  #2.1
# # # # # #print(a+c)  # Error

# # # # # print (type(a))
# # # # # print (type(b))
# # # # # print (type(c))

# # # # # #Convert Types
# # # # # a = float(a) #float
# # # # # b = int(b)
# # # # # c = int(c)
# # # # # print(a+c)

# # # # # Scope Variable - Gloal and local Variable
# # # # x = "awesome" # string

# # # # def my_function():
# # # #     x = "fantastic."
# # # #     print("Python is "+ x)

# # # # my_function()
# # # # print("Python is " + x)

# # # # #input statements 
# # # # student_name = input("Enter your name: ")

# # # # #Output statements 
# # # # print("Student name:"+ student_name)

# # # # #input and Output
# # # a = int(input("Enter a number: "))
# # # b = int(input("Enter another number: "))

# # # a = int(a)
# # # b = int(b)

# # # print(a+b)  # Output the sum of a and b

# # #python divides the operators in the following way
# # #assignments operators
# # a = 8
# # b = 2
# # v += 2
# # s -= 3

# # #Mulitplication assingment
# # m /= 2


# # #arthmetic operators
# # a = a + b #Addition 10
# # b = a - b #Subtraction 8
# # c = a * b # Multiplication 80
# # d = a / b # Division 1.25
# # e = a % b # Modulus  1
# # f = a ** b  # exponentiation 10^8
# # g = a // b  # floor division 2
# # print("Addition:", a)
# # print("Subtraction:", b)
# # print("Multiplication:", c)
# # print("Division:", d)
# # print("Modulus:", e)
# # print("Exponentiation:", f) 
# # print("Floor Division:", g) 

# # #Comparison Operators
# a = 10
# b = 10.0

# #Equal to
# print(a == b)  # True if a is Equal to b
# # a==b
# print(a == b and type(a) == type(b))  # True if a is Equal to b and both are of same type

# # Not equal to
# print(a != b)  # True if a is Not Equal to b

# #Greater than
# print(a > b)  # True if a is Greater than b

# #Gtareater than or equal to
# print(a >= b)  # True if a is Greater than or Equal to b

# #Less than or equal to
# print(a < b)  # True if a is Less than b

# #Logical Operators
# # and
# print(a > and b <15)  # True if both conditions are True
# # or
# print(a > 5 or b < 5)  # True if at least one condition is True
# # not
# print(not(a > 5))  # True if the condition is False

#Sa,ple useage of Python's math library

import math
#Square root
print(math.sqrt(16))  # Output: 4.0

#Power
print(math.pow(2, 3))  # Output: 8.0

#constant
print(math.pi)  # Output: 3.141592653589793
