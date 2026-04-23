# Task 1: To-Do List Application

tasks = []

def add_task():
    try:
        task = input("Enter task description: ").strip()
        if not task:
            raise ValueError("Task cannot be empty")
        tasks.append({"desc": task, "done": False})
        print("Task added successfully!")
    except Exception as e:
        print("Error:", e)

def view_tasks():
    try:
        if not tasks:
            print("No tasks available.")
            return
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "done" if task["done"] else "pending"
            print(f"{i}. {task['desc']} [{status}]")
    except Exception as e:
        print("Error:", e)

def mark_complete():
    try:
        view_tasks()
        index = int(input("Enter task number to mark complete: "))
        if index < 1 or index > len(tasks):
            raise IndexError("Invalid task number")
        tasks[index - 1]["done"] = True
        print("Task marked as complete!")
    except ValueError:
        print("Invalid input. Enter a number.")
    except IndexError as e:
        print(e)
    except Exception as e:
        print("Error:", e)

def delete_task():
    try:
        view_tasks()
        index = int(input("Enter task number to delete: "))
        if index < 1 or index > len(tasks):
            raise IndexError("Invalid task number")
        removed = tasks.pop(index - 1)
        print(f"Deleted: {removed['desc']}")
    except ValueError:
        print("Invalid input. Enter a number.")
    except IndexError as e:
        print(e)
    except Exception as e:
        print("Error:", e)

def main():
    while True:
        try:
            print("\n--- TO-DO MENU ---")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Complete")
            print("4. Delete Task")
            print("5. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                mark_complete()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice")

        except ValueError:
            print("Please enter a valid number")
        except Exception as e:
            print("Unexpected Error:", e)

if __name__ == "__main__":
    main()