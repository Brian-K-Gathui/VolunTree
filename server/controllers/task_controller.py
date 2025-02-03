from models import db, Task

def get_all_tasks():
    return Task.query.all()

def get_task_by_id(task_id):
    return Task.query.get(task_id)

def create_task(data):
    new_task = Task(
        title=data['title'],
        description=data['description'],
        status=data.get('status', 'pending'),
        volunteer_id=data.get('volunteer_id')  
    )
    db.session.add(new_task)
    db.session.commit()
    return new_task

def update_task(task_id, data):
    task = Task.query.get(task_id)
    if task:
        for key, value in data.items():
            setattr(task, key, value)
        db.session.commit()
    return task

def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return True
    return False
