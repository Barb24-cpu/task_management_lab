from datetime import datetime

def validate_task_title(title):
    if not title or not isinstance(title, str) or len(title.strip()) == 0:
        raise ValueError("Task title cannot be empty.")
    return True

def validate_task_description(description):
    if not description or not isinstance(description, str) or len(description.strip()) == 0:
        raise ValueError("Task description cannot be empty.")
    return True

def validate_due_date(due_date):
    if not due_date or not isinstance(due_date, str) or len(due_date.strip()) == 0:
        raise ValueError("Due date cannot be empty.")
    try:
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        raise ValueError("Invalid date format. Expected YYYY-MM-DD.")