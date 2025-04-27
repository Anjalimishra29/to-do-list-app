def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("\nNo tasks yet!")
    else:
        for idx, task in enumerate(todo_list, 1):
            status = "Done" if task['done'] else "Not Done"
            print(f"{idx}. {task['task']} [{status}]")

def add_task():
    task = input("\nEnter the task: ")
    todo_list.append({"task": task, "done": False})
    print("Task added!")

def mark_done():
    view_tasks()
    task_num = int(input("\nEnter task number to mark as done: "))
    if 0 < task_num <= len(todo_list):
        todo_list[task_num - 1]['done'] = True
        print("Task marked as done!")

def delete_task():
    view_tasks()
    task_num = int(input("\nEnter task number to delete: "))
    if 0 < task_num <= len(todo_list):
        todo_list.pop(task_num - 1)
        print("Task deleted!")

while True:
    show_menu()
    choice = input("\nEnter your choice: ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("\nThank you for using To-Do App! Goodbye! 👋")
        break
    else:
        print("Invalid choice! Please try again.")