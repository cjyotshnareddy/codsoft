tasks = []

def add_task(task):
    if task:
        tasks.append(task)
        print(f"Added: {task}")
    else:
        print("Task cannot be empty!")

def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Deleted: {removed}")
    else:
        print("Invalid task index!")

def view_tasks():
    if tasks:
        print("To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks available.")

# Example Usage
add_task("Buy groceries")
add_task("Complete project")
view_tasks()
delete_task(0)
view_tasks()
