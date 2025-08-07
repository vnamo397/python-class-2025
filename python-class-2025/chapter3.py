# # #Condition statements
# # a = 5
# # b = 10

# # if (a==b):
# #     print("a==b")
# # else:
# #     print("a!==b")

# #     #scores 0-100,>80 = A,70-79=B,60-69=C,50-59=D,<50=F
# score =int(input("Enter your score: "))

# if (score >= 80):
#     if (score <= 85):
#     print('You got A-')
# else:
#     print('You got A+')

# elif (score >= 70 and score <= 79):
#     print('You got B.')
# elif (score >= 60 and score <= 69):
#     print('You got C.')
# elif (score >= 50 and score <= 59):
#     print('You got D.')
# elif (score < 50):
#     print('You got F.')

# else:('Sure,I-BIT 2025 got F')

# result = 3+4-(2+7)/2+5*6
# print(result)
# Step 1 = 3+4 - (9)/2+5*6
# 3+4-4.5+30
# 7-4.5+30
# 2.5 + 30

# ()
# Power
# /,*
# -,+

#Loop statements
#Whike loop
# count = 1 #init counter
# while (count <= 10): 
#     print(count)
#     count += 1  # count = count + 1

# while(True):
#     print('Why always me.')

# import random
# read_int = random.randint(1,100)

# while (True):
#     answer =int(input("Enter your answer:"))

#     if(answer == read_int):
#         print("You answer it correct!")
#         break
#     else:
#         if(answer < read_int):
#             print('Your answer is less than the random number. Try again.')
#         else:
#             print('Your answer is greater than the random number. Try again.')

# print("Thank you .Bye!")

##For loop
# for counting in range(1, 11,5):  # range(start, stop, step)
#     #count <10,count+=1
#     print(counting)

# str="orrwat Vettayavong"
# for ch in str:
#     print(ch)
# data =["Vorrawat ",12,5.0,"KMUTNB"]
# for dt in data:
#     print(dt)
for i in range(1, 11,1):  # range(start, stop, step)
     if (i==5):
            continue
        print(i)
     
if(True):
      pass