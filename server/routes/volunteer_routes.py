from flask import request
from flask_restful import Resource
from controllers.volunteer_controller import get_all_volunteers, get_volunteer_by_id, create_volunteer, update_volunteer, delete_volunteer

class VolunteerResource(Resource):
    def get(self):
        volunteers, status_code = get_all_volunteers()
        return volunteers, status_code

    def post(self):
        data = request.get_json()
        volunteer, status_code = create_volunteer(data)
        return volunteer, status_code

class VolunteerByIdResource(Resource):
    def get(self, volunteer_id):
        volunteer, status_code = get_volunteer_by_id(volunteer_id)
        return volunteer, status_code

    def patch(self, volunteer_id):
        data = request.get_json()
        volunteer, status_code = update_volunteer(volunteer_id, data)
        return volunteer, status_code

    def delete(self, volunteer_id):
        response, status_code = delete_volunteer(volunteer_id)
        return response, status_code
