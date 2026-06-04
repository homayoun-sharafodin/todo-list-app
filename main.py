import json

FILE_NAME = "tasks.json"
tasks = []


def show_menu():
    print("\n===== TO-DO LIST APP =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")


def add_task():
    title = input("Enter task title: ")

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False
    }

    tasks.append(task)
    save_tasks()
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour tasks:")

    for task in tasks:
        status = "Done" if task["done"] else "Not done"
        print(f'{task["id"]}. {task["title"]} - {status}')

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def mark_task_done():
    view_tasks()

    if not tasks:
        return

    try:
        task_id = int(input("Enter task ID to mark as done: "))

        for task in tasks:
            if task["id"] == task_id:
                task["done"] = True
                save_tasks()
                print("Task marked as done.")
                return

        print("Task not found.")

    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_id = int(input("Enter task ID to delete: "))

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                save_tasks()
                print("Task deleted successfully.")
                return

        print("Task not found.")

    except ValueError:
        print("Please enter a valid number.")

def main():
    global tasks
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")


if __name__ == "__main__":
    main()