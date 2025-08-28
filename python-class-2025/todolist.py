task = []

def menu():
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. Remove Tasks")
    print("3. View Task")
    print("4. Exit")

#main loop
while True:
    menu()
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        task_name = input("Enter the task name: ")
        task.append(task_name)
        print(f"Task '{task_name}' added.")
    
    elif choice == '2':
        if not task:
            print("No tasks to remove.")
        else:
            print("Current Tasks:")
            for idx, t in enumerate(task, start=1):
                print(f"{idx}. {t}")
            task_num_input = input("Enter the task number to remove: ")
            if not task_num_input.isdigit():
                print("Please enter a valid number.")
            else:
                task_num = int(task_num_input)
                if 1 <= task_num <= len(task):
                    removed_task = task.pop(task_num - 1)
                    print(f"Task '{removed_task}' removed.")
                else:
                    print(f"Invalid task number. Please enter a number between 1 and {len(task)}.")
    
    elif choice == '3':
        if not task:
            print("No tasks available.")
        else:
            print("Current Tasks:")
            for idx, t in enumerate(task, start=1):
                print(f"{idx}. {t}")
    
    elif choice == '4':
        print("Exiting To-Do List. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select a valid option (1-4).")