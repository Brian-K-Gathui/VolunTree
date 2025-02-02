from flask import request
from flask_restful import Resource
from controllers.task_controller import (
    get_all_tasks,
    get_task_by_id,
    create_task,
    update_task,
    delete_task
)

class TaskResource(Resource):
    def get(self, task_id=None):
        if task_id:
            task = get_task_by_id(task_id)
            return task.to_dict() if task else {"error": "Task not found"}, 404
        return [task.to_dict() for task in get_all_tasks()], 200

    def post(self):
        data = request.get_json()
        task = create_task(data)
        return task.to_dict(), 201

class TaskByIdResource(Resource):
    def get(self, task_id):
        task = get_task_by_id(task_id)
        return task.to_dict() if task else {"error": "Task not found"}, 404

    def patch(self, task_id):
        data = request.get_json()
        task = update_task(task_id, data)
        return task.to_dict() if task else {"error": "Task not found"}, 404

    def delete(self, task_id):
        return {"message": "Task deleted"} if delete_task(task_id) else {"error": "Task not found"}, 404
