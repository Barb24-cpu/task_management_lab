from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str) or len(title.strip()) == 0:
        return False
    return True

def validate_task_description(description):
    if not isinstance(description, str) or len(description.strip()) == 0:
        return False
    return True

def validate_due_date(due_date):
    if not isinstance(due_date, str) or len(due_date.strip()) == 0:
        return False
    try:
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False