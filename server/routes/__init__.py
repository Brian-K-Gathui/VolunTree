from flask_restful import Api
from routes.events import EventResource, EventByIdResource
from routes.organizers import OrganizerResource, OrganizerByIdResource
from routes.volunteers import VolunteerResource, VolunteerByIdResource
from routes.tasks import TaskResource, TaskByIdResource

def register_routes(api: Api):
    """Registers all API routes with the Flask app."""
    api.add_resource(EventResource, '/events')
    api.add_resource(EventByIdResource, '/events/<int:event_id>')
    api.add_resource(OrganizerResource, '/organizers')
    api.add_resource(OrganizerByIdResource, '/organizers/<int:organizer_id>')
    api.add_resource(VolunteerResource, '/volunteers')
    api.add_resource(VolunteerByIdResource, '/volunteers/<int:volunteer_id>')
    api.add_resource(TaskResource, '/tasks')
    api.add_resource(TaskByIdResource, '/tasks/<int:task_id>')
