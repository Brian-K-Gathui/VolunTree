#!/usr/bin/env python3

# ===============================
#        FLASK APPLICATION
# ===============================

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Resource
from flask_cors import CORS

# Local imports
from config import app, db, api
from models import Organizer, Event, Volunteer, Task, event_volunteers

# ===============================
#        ROOT ENDPOINT
# ===============================
@app.route('/')
def index():
    return '<h1>VolunTree API Server</h1>'

# ===============================
#       ORGANIZER RESOURCE
# ===============================
class OrganizerResource(Resource):
    def get(self):
        """Get all organizers"""
        return make_response([org.to_dict() for org in Organizer.query.all()], 200)

    def post(self):
        """Create a new organizer"""
        data = request.get_json()
        organizer = Organizer(
            name=data.get('name'),
            contact_name=data.get('contact_name'),
            contact_phone=data.get('contact_phone'),
            contact_email=data.get('contact_email')
        )
        db.session.add(organizer)
        db.session.commit()
        return make_response(organizer.to_dict(), 201)

api.add_resource(OrganizerResource, '/organizers')

# ===============================
#       ORGANIZER BY ID
# ===============================
class OrganizerById(Resource):
    def get(self, id):
        """Get an organizer by ID"""
        organizer = Organizer.query.get(id)
        if organizer:
            return make_response(organizer.to_dict(), 200)
        return make_response({'error': 'Organizer not found'}, 404)

    def patch(self, id):
        """Update an organizer"""
        organizer = Organizer.query.get(id)
        if organizer:
            data = request.get_json()
            for key, value in data.items():
                setattr(organizer, key, value)
            db.session.commit()
            return make_response(organizer.to_dict(), 200)
        return make_response({'error': 'Organizer not found'}, 404)

    def delete(self, id):
        """Delete an organizer"""
        organizer = Organizer.query.get(id)
        if organizer:
            db.session.delete(organizer)
            db.session.commit()
            return make_response({'message': 'Organizer deleted successfully'}, 200)
        return make_response({'error': 'Organizer not found'}, 404)

api.add_resource(OrganizerById, '/organizers/<int:id>')

# ===============================
#       EVENT RESOURCE
# ===============================
class EventResource(Resource):
    def get(self):
        """Get all events"""
        return make_response([event.to_dict() for event in Event.query.all()], 200)

    def post(self):
        """Create a new event"""
        data = request.get_json()
        event = Event(
            name=data.get('name'),
            date=data.get('date'),
            location=data.get('location'),
            organizer_id=data.get('organizer_id')
        )
        db.session.add(event)
        db.session.commit()
        return make_response(event.to_dict(), 201)

api.add_resource(EventResource, '/events')

# ===============================
#       VOLUNTEER RESOURCE
# ===============================
class VolunteerResource(Resource):
    def get(self):
        """Get all volunteers"""
        return make_response([volunteer.to_dict() for volunteer in Volunteer.query.all()], 200)

    def post(self):
        """Create a new volunteer"""
        data = request.get_json()
        volunteer = Volunteer(
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone')
        )
        db.session.add(volunteer)
        db.session.commit()
        return make_response(volunteer.to_dict(), 201)

api.add_resource(VolunteerResource, '/volunteers')

# ===============================
#       TASK RESOURCE
# ===============================
class TaskResource(Resource):
    def get(self):
        """Get all tasks"""
        return make_response([task.to_dict() for task in Task.query.all()], 200)

    def post(self):
        """Create a new task"""
        data = request.get_json()
        task = Task(
            title=data.get('title'),
            description=data.get('description'),
            status=data.get('status', 'pending'),
            event_id=data.get('event_id'),
            volunteer_id=data.get('volunteer_id')
        )
        db.session.add(task)
        db.session.commit()
        return make_response(task.to_dict(), 201)

api.add_resource(TaskResource, '/tasks')

# ===============================
#       ERROR HANDLING
# ===============================
@app.errorhandler(404)
def not_found(error):
    return make_response({'error': 'Not found'}, 404)

# ===============================
#       RUN THE APPLICATION
# ===============================
if __name__ == '__main__':
    app.run(port=5555, debug=True)
