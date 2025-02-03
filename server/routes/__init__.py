from flask_restful import Api
from routes.admin_routes import AdminSignup, AdminLogin, AdminProfile
from routes.event_routes import EventResource, EventByIdResource
from routes.organizer_routes import OrganizerResource, OrganizerByIdResource
from routes.volunteer_routes import VolunteerResource, VolunteerByIdResource
from routes.task_routes import TaskResource, TaskByIdResource

def register_routes(api: Api):
    api.add_resource(EventResource, '/events')
    api.add_resource(EventByIdResource, '/events/<int:event_id>')
    
    api.add_resource(OrganizerResource, '/organizers')
    api.add_resource(OrganizerByIdResource, '/organizers/<int:organizer_id>')
    
    api.add_resource(VolunteerResource, '/volunteers')
    api.add_resource(VolunteerByIdResource, '/volunteers/<int:volunteer_id>')
    
    api.add_resource(TaskResource, '/tasks')
    api.add_resource(TaskByIdResource, '/tasks/<int:task_id>')

    api.add_resource(AdminSignup, '/admin/signup')
    api.add_resource(AdminLogin, '/admin/login')
    api.add_resource(AdminProfile, '/admin/profile')
