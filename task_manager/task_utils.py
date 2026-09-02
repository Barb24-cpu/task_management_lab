from datetime import datetime

# Import validation functions
from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
   def add_task(title, description, due_date):
    if not validate_task_title(title) or not validate_task_description(description) or not validate_due_date(due_date):
        print("Validation failed. Task not added.")
        return False

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")
    return True
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
   def mark_task_as_complete(index, tasks=tasks):
    try:
        idx = int(index) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["completed"] = True
            print("Task marked as complete!")
            return True
        else:
            print("Invalid task number.")
            return False
    except ValueError:
        print("Invalid index entered.")
        return False
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
   pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks.")
    else:
        for idx, task in enumerate(pending, 1):
            print(f"{idx}. {task['title']} - {task['description']} (Due: {task['due_date']})")
    return pending

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
  if not tasks:
        print("No tasks available.")
        return 0.0
    completed = sum(1 for t in tasks if t["completed"])
    progress = (completed / len(tasks)) * 100
    print(f"Progress: {progress:.2f}%")
    return progress