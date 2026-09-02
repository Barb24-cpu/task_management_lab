from datetime import datetime

def validate_task_title(title):
    if title is None or not isinstance(title, str):
        return False
    if len(title.strip()) == 0:
        return False
    return True

def validate_task_description(description):
    if description is None or not isinstance(description, str):
        return False
    if len(description.strip()) == 0:
        return False
    return True

def validate_due_date(due_date):
    if due_date is None or not isinstance(due_date, str):
        return False
    if len(due_date.strip()) == 0:
        return False
    try:
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
        return True
    except ValueError:
        return False