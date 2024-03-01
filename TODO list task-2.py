import os

# Function to display menu
def display_menu():
    print("\nTODO LIST MENU:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Mark task as undone")
    print("5. Remove task")
    print("6. Exit")

# Function to load tasks from file
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = [line.strip().split(",") for line in file.readlines()]
        return {int(task[0]): {"task": task[1], "done": task[2] == "True"} for task in tasks}
    else:
        return {}

# Function to save tasks to file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task_id, task_info in tasks.items():
            file.write(f"{task_id},{task_info['task']},{task_info['done']}\n")

# Function to view tasks
def view_tasks(tasks):
    if tasks:
        print("\nTASKS:")
        for task_id, task_info in tasks.items():
            print(f"{task_id}. {'[X]' if task_info['done'] else '[ ]'} {task_info['task']}")
    else:
        print("No tasks yet!")

# Function to add task
def add_task(tasks):
    task = input("Enter task: ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"task": task, "done": False}
    print("Task added successfully!")

# Function to mark task as done or undone
def mark_task(tasks, done=True):
    view_tasks(tasks)
    task_id = int(input("Enter task ID: "))
    if task_id in tasks:
        tasks[task_id]["done"] = done
        print("Task marked as done!" if done else "Task marked as undone!")
    else:
        print("Invalid task ID!")

# Function to remove task
def remove_task(tasks):
    view_tasks(tasks)
    task_id = int(input("Enter task ID to remove: "))
    if task_id in tasks:
        del tasks[task_id]
        print("Task removed successfully!")
    else:
        print("Invalid task ID!")

# Main function to start the program
def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task(tasks)
        elif choice == '4':
            mark_task(tasks, done=False)
        elif choice == '5':
            remove_task(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()
