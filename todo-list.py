# To-Do List Application:

tasks = []

while True:
    print("\nTodo List:")
    print("==========")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    
    print("\nOptions:")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")
    elif choice == "2":
        if tasks:
            index = int(input("Enter the index of the task to mark as completed: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index] = f"[DONE] {tasks[index]}"
                print("Task marked as completed!")
            else:
                print("Invalid index!")
        else:
            print("No tasks available!")
    elif choice == "3":
        if tasks:
            index = int(input("Enter the index of the task to delete: ")) - 1
            if 0 <= index < len(tasks):
                deleted_task = tasks.pop(index)
                print(f"Task '{deleted_task}' deleted successfully!")
            else:
                print("Invalid index!")
        else:
            print("No tasks available!")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")