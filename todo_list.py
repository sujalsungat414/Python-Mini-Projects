todo_list = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done") 
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(todo_list):
            status = "✅" if task["done"] else "❌"
            print(f"{idx + 1}. {task['task']} [{status}]")  # ✅ Fix: use single quotes inside f-string

def add_task():
    task_name = input("Enter your task: ")
    todo_list.append({"task": task_name, "done": False})  # ✅ Fix: Add "done": False
    print("Task added!")

def mark_task_done():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: "))
        todo_list[task_num - 1]["done"] = True
        print("Task marked as done.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        removed = todo_list.pop(task_num - 1)
        print(f"Task '{removed['task']}' deleted.")  # ✅ Fix: use single quotes
    except (ValueError, IndexError):
        print("Invalid task number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_task_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please select from 1-5.")
