from flask import request
from flask_restful import Resource
from controllers.task_controller import get_all_tasks, get_task_by_id, create_task, update_task, delete_task

class TaskResource(Resource):
    def get(self):
        tasks, status_code = get_all_tasks()
        return tasks, status_code

    def post(self):
        data = request.get_json()
        task, status_code = create_task(data)
        return task, status_code

class TaskByIdResource(Resource):
    def get(self, task_id):
        task, status_code = get_task_by_id(task_id)
        return task, status_code

    def patch(self, task_id):
        data = request.get_json()
        task, status_code = update_task(task_id, data)
        return task, status_code

    def delete(self, task_id):
        response, status_code = delete_task(task_id)
        return response, status_code
