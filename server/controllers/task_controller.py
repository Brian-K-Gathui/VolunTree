from models import db, Task

def get_all_tasks():
    """Fetch all tasks from the database."""
    return Task.query.all()

def get_task_by_id(task_id):
    """Retrieve a single task by ID."""
    return Task.query.get(task_id)

def create_task(data):
    """Create a new task and associate it with an event and optionally a volunteer."""
    new_task = Task(
        title=data['title'],
        description=data['description'],
        status=data.get('status', 'pending'),  # Default status is 'pending'
        event_id=data['event_id'],
        volunteer_id=data.get('volunteer_id')  # Can be None if the task is unassigned
    )
    db.session.add(new_task)
    db.session.commit()
    return new_task

def update_task(task_id, data):
    """Update an existing task with new details."""
    task = Task.query.get(task_id)
    if task:
        for key, value in data.items():
            setattr(task, key, value)
        db.session.commit()
    return task

def delete_task(task_id):
    """Delete a task from the database."""
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return True
    return False
