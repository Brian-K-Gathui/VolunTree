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
    return "<h1>VolunTree API Server is Running! 🌱</h1>\n"

# ===============================
#       ORGANIZER RESOURCE
# ===============================
class OrganizerResource(Resource):
    def get(self):
        """Get all organizers"""
        organizers = [org.to_dict() for org in Organizer.query.all()]
        print(f"📢 Fetching {len(organizers)} organizers...")  
        return make_response(organizers, 200)

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
        print(f"✅ Organizer '{organizer.name}' added successfully!")
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
            print(f"🔎 Organizer Found: {organizer.name}")
            return make_response(organizer.to_dict(), 200)
        print("❌ Organizer not found!")
        return make_response({'error': 'Organizer not found'}, 404)

    def patch(self, id):
        """Update an organizer"""
        organizer = Organizer.query.get(id)
        if organizer:
            data = request.get_json()
            for key, value in data.items():
                setattr(organizer, key, value)
            db.session.commit()
            print(f"✏️ Organizer '{organizer.name}' updated successfully!")
            return make_response(organizer.to_dict(), 200)
        print("❌ Organizer not found for update!")
        return make_response({'error': 'Organizer not found'}, 404)

    def delete(self, id):
        """Delete an organizer"""
        organizer = Organizer.query.get(id)
        if organizer:
            db.session.delete(organizer)
            db.session.commit()
            print(f"🗑️ Organizer '{organizer.name}' deleted!")
            return make_response({'message': 'Organizer deleted successfully'}, 200)
        print("❌ Organizer not found for deletion!")
        return make_response({'error': 'Organizer not found'}, 404)

api.add_resource(OrganizerById, '/organizers/<int:id>')

# ===============================
#       EVENT RESOURCE
# ===============================
class EventResource(Resource):
    def get(self):
        """Get all events"""
        events = [event.to_dict() for event in Event.query.all()]
        print(f"📢 Fetching {len(events)} events...")
        return make_response(events, 200)

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
        print(f"✅ Event '{event.name}' created successfully!")
        return make_response(event.to_dict(), 201)

api.add_resource(EventResource, '/events')

# ===============================
#       VOLUNTEER RESOURCE
# ===============================
class VolunteerResource(Resource):
    def get(self):
        """Get all volunteers"""
        volunteers = [volunteer.to_dict() for volunteer in Volunteer.query.all()]
        print(f"📢 Fetching {len(volunteers)} volunteers...")
        return make_response(volunteers, 200)

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
        print(f"✅ Volunteer '{volunteer.name}' registered successfully!")
        return make_response(volunteer.to_dict(), 201)

api.add_resource(VolunteerResource, '/volunteers')

# ===============================
#       TASK RESOURCE
# ===============================
class TaskResource(Resource):
    def get(self):
        """Get all tasks"""
        tasks = [task.to_dict() for task in Task.query.all()]
        print(f"📢 Fetching {len(tasks)} tasks...")
        return make_response(tasks, 200)

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
        print(f"✅ Task '{task.title}' created successfully!")
        return make_response(task.to_dict(), 201)

api.add_resource(TaskResource, '/tasks')

# ===============================
#       ERROR HANDLING
# ===============================
@app.errorhandler(404)
def not_found(error):
    print("❌ 404 Error: Route not found!")
    return make_response({'error': 'Not found'}, 404)

# ===============================
#       RUN THE APPLICATION
# ===============================
if __name__ == '__main__':
    print("\n🚀 VolunTree API is starting...")
    print("_____________________________________________\n")
    app.run(port=5555, debug=True)
