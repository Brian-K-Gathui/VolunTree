from flask import request
from flask_restful import Resource
from controllers.event_controller import get_all_events, get_event_by_id, create_event, update_event, delete_event

class EventResource(Resource):
    def get(self):
        events, status_code = get_all_events()
        return events, status_code

    def post(self):
        data = request.get_json()
        event, status_code = create_event(data)
        return event, status_code

class EventByIdResource(Resource):
    def get(self, event_id):
        event, status_code = get_event_by_id(event_id)
        return event, status_code

    def patch(self, event_id):
        data = request.get_json()
        event, status_code = update_event(event_id, data)
        return event, status_code

    def delete(self, event_id):
        response, status_code = delete_event(event_id)
        return response, status_code
