# Import necessary modules from Flask and SQLAlchemy
from flask_sqlalchemy import SQLAlchemy  # ORM (Object-Relational Mapper) for handling database interactions
from sqlalchemy_serializer import SerializerMixin  # Enables easy serialization of objects to JSON
from sqlalchemy.orm import validates  # Provides validation for model attributes
from sqlalchemy.ext.associationproxy import association_proxy  # Helps manage many-to-many relationships

from config import db  # Importing database instance from config.py

# ============================== #
#        MODELS FOR VOLUNTREE    #
# ============================== #

# ------------------------------
# ORGANIZER MODEL
# ------------------------------
class Organizer(db.Model, SerializerMixin):
    """
    Organizer Model: Represents an organization that hosts volunteer-driven events.

    Relationships:
    - One-to-Many with Events: An Organizer can host multiple events.
    """

    __tablename__ = 'organizers'  # Explicitly sets the table name in the database

    # Define serialization rules to avoid circular references
    serialize_rules = ('-events.organizer',)

    # Define Columns
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each organizer
    name = db.Column(db.String(255), nullable=False)  # Name of the organization
    contact_name = db.Column(db.String(255), nullable=False)  # Main contact person's name
    contact_phone = db.Column(db.String(20), nullable=False)  # Contact phone number
    contact_email = db.Column(db.String(120), nullable=False, unique=True)  # Unique contact email

    # Define Relationships
    events = db.relationship('Event', back_populates='organizer', cascade='all, delete-orphan')
    # - An Organizer can have multiple Events.
    # - If an Organizer is deleted, all related Events will also be deleted.

    # Validations for required fields
    @validates('name', 'contact_name', 'contact_phone', 'contact_email')
    def validate_not_empty(self, key, value):
        """Ensures that no field is left empty or contains only whitespace."""
        if not value.strip():
            raise ValueError(f'{key.capitalize()} cannot be empty')

        if key == 'contact_email' and '@' not in value:
            raise ValueError('Invalid email format')

        return value

    def __repr__(self):
        """Returns a string representation of an Organizer instance."""
        return f'<Organizer {self.id}: {self.name}>'


# ------------------------------
# EVENT MODEL
# ------------------------------
class Event(db.Model, SerializerMixin):
    """
    Event Model: Represents an event hosted by an organization.

    Relationships:
    - Many-to-One with Organizer: Each Event is associated with one Organizer.
    - One-to-Many with Tasks: An Event can have multiple Tasks.
    - Many-to-Many with Volunteers: Volunteers can participate in multiple Events.
    """

    __tablename__ = 'events'

    # Define serialization rules to avoid circular references
    serialize_rules = ('-organizer.events', '-tasks.event', '-volunteers.events')

    # Define Columns
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each event
    name = db.Column(db.String(255), nullable=False)  # Name of the event
    date = db.Column(db.Date, nullable=False)  # Event date
    location = db.Column(db.String(255), nullable=False)  # Event location

    # Foreign Key linking to Organizer
    organizer_id = db.Column(db.Integer, db.ForeignKey('organizers.id'), nullable=False)

    # Define Relationships
    organizer = db.relationship('Organizer', back_populates='events')  # Event belongs to an Organizer
    tasks = db.relationship('Task', back_populates='event', cascade='all, delete-orphan')  # Event has many Tasks
    volunteers = db.relationship('Volunteer', secondary='event_volunteers', back_populates='events')
    # - Many-to-Many: An Event can have multiple Volunteers and vice versa.

    @validates('name', 'location')
    def validate_not_empty(self, key, value):
        """Ensures that the event name and location are not empty."""
        if not value.strip():
            raise ValueError(f'{key.capitalize()} cannot be empty')
        return value

    def __repr__(self):
        """Returns a string representation of an Event instance."""
        return f'<Event {self.id}: {self.name}>'


# ------------------------------
# VOLUNTEER MODEL
# ------------------------------
class Volunteer(db.Model, SerializerMixin):
    """
    Volunteer Model: Represents volunteers who participate in events.

    Relationships:
    - Many-to-Many with Events: A Volunteer can participate in multiple Events.
    - One-to-Many with Tasks: A Volunteer can be assigned multiple Tasks.
    """

    __tablename__ = 'volunteers'

    # Define serialization rules to avoid circular references
    serialize_rules = ('-tasks.volunteer', '-events.volunteers')

    # Define Columns
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each volunteer
    name = db.Column(db.String(255), nullable=False)  # Volunteer name
    email = db.Column(db.String(120), nullable=False, unique=True)  # Unique volunteer email
    phone = db.Column(db.String(20), nullable=False)  # Volunteer phone number

    # Define Relationships
    events = db.relationship('Event', secondary='event_volunteers', back_populates='volunteers')
    # - Many-to-Many: Volunteers can participate in multiple Events.
    tasks = db.relationship('Task', back_populates='volunteer', cascade='all, delete-orphan')
    # - One-to-Many: A Volunteer can be assigned multiple Tasks.

    @validates('name', 'phone', 'email')
    def validate_not_empty(self, key, value):
        """Ensures that no field is empty and validates email format."""
        if not value.strip():
            raise ValueError(f'{key.capitalize()} cannot be empty')

        if key == 'email' and '@' not in value:
            raise ValueError('Invalid email format')

        return value

    def __repr__(self):
        """Returns a string representation of a Volunteer instance."""
        return f'<Volunteer {self.id}: {self.name}>'


# ------------------------------
# TASK MODEL
# ------------------------------
class Task(db.Model, SerializerMixin):
    """
    Task Model: Represents tasks assigned to volunteers within an event.

    Relationships:
    - Many-to-One with Event: A Task belongs to an Event.
    - Many-to-One with Volunteer: A Task is assigned to a Volunteer.
    """

    __tablename__ = 'tasks'

    # Define serialization rules to avoid circular references
    serialize_rules = ('-event.tasks', '-volunteer.tasks')

    # Define Columns
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each task
    title = db.Column(db.String(255), nullable=False)  # Task title
    description = db.Column(db.Text, nullable=False)  # Task description
    status = db.Column(db.String(50), nullable=False, default='pending')  # Task status (e.g., "pending", "completed")

    # Foreign Keys linking to Event and Volunteer
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteers.id'), nullable=True)

    # Define Relationships
    event = db.relationship('Event', back_populates='tasks')  # Task belongs to an Event
    volunteer = db.relationship('Volunteer', back_populates='tasks')  # Task is assigned to a Volunteer

    @validates('title', 'description', 'status')
    def validate_not_empty(self, key, value):
        """Ensures that title, description, and status are not empty."""
        if not value.strip():
            raise ValueError(f'{key.capitalize()} cannot be empty')
        return value

    def __repr__(self):
        """Returns a string representation of a Task instance."""
        return f'<Task {self.id}: {self.title}>'


# ------------------------------
# ASSOCIATION TABLE: EVENT-VOLUNTEERS
# ------------------------------
# This table establishes a many-to-many relationship between Events and Volunteers.
event_volunteers = db.Table('event_volunteers',
    db.Column('event_id', db.Integer, db.ForeignKey('events.id'), primary_key=True),
    db.Column('volunteer_id', db.Integer, db.ForeignKey('volunteers.id'), primary_key=True)
)
