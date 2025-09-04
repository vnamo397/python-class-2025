a = int(input("Enter first number:"))
b = int(input("Enter second number:"))


#main program
if  __name__== "__main__":
    print("Total:", a + b)
          

try:
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))


    #main program
    if  __name__== "__main__":
        print("Total:", a / b)
    
except ValueError:
    print("You have entered invalid input")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except:
    print("Something went wrong")

finally:
    print("Execution completed")