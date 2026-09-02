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

def add_task(title, description, due_date, task_list=None):
    if task_list is None:
        task_list = tasks

    if not validate_task_title(title) or not validate_task_description(description) or not validate_due_date(due_date):
        print("Validation failed.")
        return False

    task = {
        "title": title.strip() if isinstance(title, str) else title,
        "description": description.strip() if isinstance(description, str) else description,
        "due_date": due_date.strip() if isinstance(due_date, str) else due_date,
        "completed": False
    }
    task_list.append(task)
    print("Task added successfully!")
    return True

def mark_task_as_complete(index, task_list=None):
    if task_list is None:
        task_list = tasks
    try:
        idx = int(index) - 1
        if 0 <= idx < len(task_list):
            task_list[idx]["completed"] = True
            print("Task marked as complete!")
            return True
        print("Invalid task number.")
        return False
    except (ValueError, TypeError):
        print("Invalid index entered.")
        return False

def view_pending_tasks(task_list=None):
    if task_list is None:
        task_list = tasks
    pending = [t for t in task_list if not t.get("completed", False)]
    if not pending:
        print("No pending tasks.")
        return []
    for idx, task in enumerate(pending, 1):
        print(f"{idx}. {task['title']} - {task['description']} (Due: {task['due_date']})")
    return pending

def calculate_progress(task_list=None):
    if task_list is None:
        task_list = tasks
    if not task_list:
        print("No working currently")
        return 0.0
    completed = sum(1 for t in task_list if t.get("completed", False))
    progress = (completed / len(task_list)) * 100.0
    print(f"Progress: {progress:.2f}%")
    return progress