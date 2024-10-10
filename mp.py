import json
import os

# Function to display tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "Done" if task['completed'] else "Pending"
            print(f"{i}. {task['name']} - {status}")

# Function to add a new task
def add_task(tasks):
    name = input("Enter task name: ")
    tasks.append({'name': name, 'completed': False})

# Function to mark a task as completed
def complete_task(tasks):
    show_tasks(tasks)
    task_num = int(input("Enter task number to mark as completed: "))
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1]['completed'] = True
    else:
        print("Invalid task number.")

# Function to save tasks to a JSON file
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to load tasks from a JSON file
def load_tasks(filename="tasks.json"):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu")
        print("1. View Task")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

