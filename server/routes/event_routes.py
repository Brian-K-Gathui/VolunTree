from flask import request
from flask_restful import Resource
from controllers.event_controller import (
    get_all_events,
    get_event_by_id,
    create_event,
    update_event,
    delete_event
)

class EventResource(Resource):
    def get(self, event_id=None):
        if event_id:
            event = get_event_by_id(event_id)
            return event.to_dict() if event else {"error": "Event not found"}, 404
        return [event.to_dict() for event in get_all_events()], 200

    def post(self):
        data = request.get_json()
        event = create_event(data)
        return event.to_dict(), 201

class EventByIdResource(Resource):
    def get(self, event_id):
        event = get_event_by_id(event_id)
        return event.to_dict() if event else {"error": "Event not found"}, 404

    def patch(self, event_id):
        data = request.get_json()
        event = update_event(event_id, data)
        return event.to_dict() if event else {"error": "Event not found"}, 404

    def delete(self, event_id):
        return {"message": "Event deleted"} if delete_event(event_id) else {"error": "Event not found"}, 404
