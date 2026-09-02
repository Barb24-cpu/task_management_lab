try:
    from task_manager.validation import (
        validate_task_title,
        validate_task_description,
        validate_due_date
    )
except ModuleNotFoundError:
    from validation import (
        validate_task_title,
        validate_task_description,
        validate_due_date
    )

tasks = []

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

def mark_task_as_complete(index):
    try:
        idx = int(index) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["completed"] = True
            print("Task marked as complete!")
            return True
        else:
            print("Invalid task number.")
            return False
    except (ValueError, TypeError):
        print("Invalid index entered.")
        return False

def view_pending_tasks():
    pending = [t for t in tasks if not t.get("completed", False)]
    if not pending:
        print("No pending tasks.")
        return []
    for idx, task in enumerate(pending, 1):
        print(f"{idx}. {task['title']} - {task['description']} (Due: {task['due_date']})")
    return pending

def calculate_progress():
    if not tasks or len(tasks) == 0:
        print("No working currently")
        return 0.0
    completed = sum(1 for t in tasks if t.get("completed", False))
    progress = (completed / len(tasks)) * 100
    print(f"Progress: {progress:.2f}%")
    return progress