from models import db, Task

def get_all_tasks():
    return [task.serialize() for task in Task.query.all()], 200

def get_task_by_id(task_id):
    task = Task.query.get(task_id)
    if not task:
        return {"error": "Task not found"}, 404
    return task.serialize(), 200

def create_task(data):
    new_task = Task(
        title=data['title'],
        description=data['description'],
        status=data.get('status', 'pending'),
        event_id=data.get('event_id'),
        volunteer_id=data.get('volunteer_id')
    )
    db.session.add(new_task)
    db.session.commit()
    return new_task.serialize(), 201

def update_task(task_id, data):
    task = Task.query.get(task_id)
    if not task:
        return {"error": "Task not found"}, 404

    for key, value in data.items():
        setattr(task, key, value)
    
    db.session.commit()
    return task.serialize(), 200

def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return {"error": "Task not found"}, 404

    db.session.delete(task)
    db.session.commit()
    return {"message": "Task deleted successfully"}, 200
