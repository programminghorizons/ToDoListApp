# Create an empty list to store the tasks and their status
todo_list = []


# Function to Add a New Task
def add_task():
    task = input("Enter a task: ")
    todo_list.append({"Task": task, "Status": "pending"})
    print("New Task Added Successfully!\n")


# Function to View All Tasks
def view_task():
    print("Your Todo List: ")
    if len(todo_list) == 0:
        print("No pending tasks!")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}: {task['Task']} - {task['Status']}")
    print("\n")


# Function to Remove a Task
def remove_task():
    if len(todo_list) == 0:
        print("List is Empty!")
    else:
        try:
            search_index = int(input("Enter the task number that you want to remove: ")) - 1
            if 0 <= search_index < len(todo_list):
                removed_task = todo_list.pop(search_index)
                print(f"Task Removed: {removed_task['Task']}")
            else:
                print("Invalid Task Number.")
        except ValueError:
            print("Please Enter a Valid Task Number.")


#Function to Mark a Task as Done
def mark_done():
    if len(todo_list) == 0:
        print("List is Empty!")
    else:
        try:
            search_index = int(input("Enter the task number that you want to mark as complete: ")) - 1
            if 0 <= search_index < len(todo_list):
                todo_list[search_index]['Status'] = 'done'
                print(f"Task {todo_list[search_index]['Task']} has been marked as Done.")
            else:
                print("Invalid Task Number.")
        except ValueError:
            print("Please Enter a Valid Task Number.")


# Function to Display a Menu
def menu():
    while(True):
        print("*** Main Menu ***")
        print("1. Add a New Task")
        print("2. View All Tasks")
        print("3. Remove a Task")
        print("4. Mark a Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print("Exiting the application...")
            exit()
        else:
            print("Invalid choice! Try again!!!")


menu()
