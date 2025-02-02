from flask import request
from flask_restful import Resource
from controllers.organizer_controller import (
    get_all_organizers,
    get_organizer_by_id,
    create_organizer,
    update_organizer,
    delete_organizer
)

class OrganizerResource(Resource):
    def get(self, organizer_id=None):
        if organizer_id:
            organizer = get_organizer_by_id(organizer_id)
            return organizer.to_dict() if organizer else {"error": "Organizer not found"}, 404
        return [org.to_dict() for org in get_all_organizers()], 200

    def post(self):
        data = request.get_json()
        organizer = create_organizer(data)
        return organizer.to_dict(), 201

class OrganizerByIdResource(Resource):
    def get(self, organizer_id):
        organizer = get_organizer_by_id(organizer_id)
        return organizer.to_dict() if organizer else {"error": "Organizer not found"}, 404

    def patch(self, organizer_id):
        data = request.get_json()
        organizer = update_organizer(organizer_id, data)
        return organizer.to_dict() if organizer else {"error": "Organizer not found"}, 404

    def delete(self, organizer_id):
        return {"message": "Organizer deleted"} if delete_organizer(organizer_id) else {"error": "Organizer not found"}, 404
