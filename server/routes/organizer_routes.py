from flask import request
from flask_restful import Resource
from controllers.organizer_controller import get_all_organizers, get_organizer_by_id, create_organizer, update_organizer, delete_organizer

class OrganizerResource(Resource):
    def get(self):
        organizers, status_code = get_all_organizers()
        return organizers, status_code

    def post(self):
        data = request.get_json()
        organizer, status_code = create_organizer(data)
        return organizer, status_code

class OrganizerByIdResource(Resource):
    def get(self, organizer_id):
        organizer, status_code = get_organizer_by_id(organizer_id)
        return organizer, status_code

    def patch(self, organizer_id):
        data = request.get_json()
        organizer, status_code = update_organizer(organizer_id, data)
        return organizer, status_code

    def delete(self, organizer_id):
        response, status_code = delete_organizer(organizer_id)
        return response, status_code
