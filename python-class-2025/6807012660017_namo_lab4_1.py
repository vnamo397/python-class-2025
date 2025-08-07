my_list = []
while True:
    user_input = input("Enter something(type 'end' or'END): ")
    if user_input.lower() == 'end':
        break
    my_list.append(user_input)
    
for idx, item in enumerate(my_list,start=1):
    print(f"Item {idx}: {item}")