even_count = 0
odd_count = 0

while True:
    try:
        num_input = input("Enter an integer (0 to quit): ")
        num = float(num_input)
        num_rounded = round(num)
        if num_rounded == 0:
            break
        if num_rounded < 0:
            print("Negative numbers are not allowed. Please enter a non-negative number.")
            continue
        if num_rounded % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    except ValueError:
        print("Invalid input. Please enter a number.")

print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
