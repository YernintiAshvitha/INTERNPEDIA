import os

def display_menu():
    """Display the menu options for the to-do list."""
    print("\nTODO LIST MENU:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Mark task as undone")
    print("5. Remove task")
    print("6. Exit")

def load_tasks():
    """
    Load tasks from a file if it exists, otherwise return an empty dictionary.

    Returns:
        dict: A dictionary containing tasks loaded from the file.
    """
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = [line.strip().split(",") for line in file.readlines()]
        return {int(task[0]): {"task": task[1], "done": task[2] == "True"} for task in tasks}
    else:
        return {}

def save_tasks(tasks):
    """
    Save tasks to a file.

    Args:
        tasks (dict): A dictionary containing tasks to be saved.
    """
    with open("tasks.txt", "w") as file:
        for task_id, task_info in tasks.items():
            file.write(f"{task_id},{task_info['task']},{task_info['done']}\n")

def view_tasks(tasks):
    """
    Display all tasks.

    Args:
        tasks (dict): A dictionary containing tasks to be displayed.
    """
    if tasks:
        print("\nTASKS:")
        for task_id, task_info in tasks.items():
            print(f"{task_id}. {'[X]' if task_info['done'] else '[ ]'} {task_info['task']}")
    else:
        print("No tasks yet!")

def add_task(tasks):
    """
    Add a new task.

    Args:
        tasks (dict): A dictionary containing tasks to which a new task will be added.
    """
    task = input("Enter task: ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"task": task, "done": False}
    print("Task added successfully!")

def mark_task(tasks, done=True):
    """
    Mark a task as done or undone.

    Args:
        tasks (dict): A dictionary containing tasks to be marked.
        done (bool, optional): Whether to mark the task as done (True) or undone (False). Defaults 
