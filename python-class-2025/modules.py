def factorial(n):
    if n <=1:
        print(1)
        return 1
    else:
        print(f"{n} *")
        return n * factorial(n-1)
    
print("Factorial of 5 is:",factorial(5))