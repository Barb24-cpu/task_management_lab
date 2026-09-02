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
    None
    print("Task marked as complete!")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    None

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    None
    return progress