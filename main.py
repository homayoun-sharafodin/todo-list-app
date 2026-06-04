def show_menu():
    print("\n===== TO-DO LIST APP =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print("Add task feature coming soon...")
        elif choice == "2":
            print("View tasks feature coming soon...")
        elif choice == "3":
            print("Mark task as done feature coming soon...")
        elif choice == "4":
            print("Delete task feature coming soon...")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")


if __name__ == "__main__":
    main()