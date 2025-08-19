# To-Do List Project (Console Version)

tasks = []

def show_menu():
    print("\n📌 To-Do List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("✅ No tasks available!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✔️ Done" if task['done'] else "❌ Pending"
            print(f"{i}. {task['task']} [{status}]")

def add_task():
    task_name = input("Enter task: ")
    tasks.append({"task": task_name, "done": False})
    print(f"✅ Task '{task_name}' added!")

def mark_done():
    view_tasks()
    try:
        task_no = int(input("Enter task number to mark as done: "))
        tasks[task_no - 1]['done'] = True
        print("✔️ Task marked as done!")
    except (IndexError, ValueError):
        print("❌ Invalid task number!")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_no - 1)
        print(f"🗑️ Task '{removed['task']}' deleted!")
    except (IndexError, ValueError):
        print("❌ Invalid task number!")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option: ")
    
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("👋 Exiting To-Do List. Goodbye!")
        break
    else:
        print("❌ Invalid choice! Please try again.")
