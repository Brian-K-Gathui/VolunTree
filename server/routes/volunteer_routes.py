from flask import request
from flask_restful import Resource
from controllers.volunteer_controller import (
    get_all_volunteers,
    get_volunteer_by_id,
    create_volunteer,
    update_volunteer,
    delete_volunteer
)

class VolunteerResource(Resource):
    def get(self, volunteer_id=None):
        if volunteer_id:
            volunteer = get_volunteer_by_id(volunteer_id)
            return volunteer.to_dict() if volunteer else {"error": "Volunteer not found"}, 404
        return [volunteer.to_dict() for volunteer in get_all_volunteers()], 200

    def post(self):
        data = request.get_json()
        volunteer = create_volunteer(data)
        return volunteer.to_dict(), 201

class VolunteerByIdResource(Resource):
    def get(self, volunteer_id):
        volunteer = get_volunteer_by_id(volunteer_id)
        return volunteer.to_dict() if volunteer else {"error": "Volunteer not found"}, 404

    def patch(self, volunteer_id):
        data = request.get_json()
        volunteer = update_volunteer(volunteer_id, data)
        return volunteer.to_dict() if volunteer else {"error": "Volunteer not found"}, 404

    def delete(self, volunteer_id):
        return {"message": "Volunteer deleted"} if delete_volunteer(volunteer_id) else {"error": "Volunteer not found"}, 404
