from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
# from sqlalchemy.ext.associationproxy import association_proxy  # Uncomment only if you need it
from werkzeug.security import generate_password_hash, check_password_hash

from config import db


class Admin(db.Model, SerializerMixin):
    """
    Admin Model: Represents administrative users who manage the VolunTree platform.

    Attributes:
    - `first_name` (String): Admin's first name.
    - `last_name` (String): Admin's last name.
    - `email` (String): Admin's unique email address (must follow firstname.lastname@gmail.com format).
    - `username` (String): Unique username for authentication.
    - `password_hash` (String): Hashed password for secure authentication.
    
    Authentication:
    - Passwords are stored securely using hashing.
    - Admins log in using their username and password.
    - JWT authentication is used to manage secure sessions.
    """

    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        """Hashes and stores the admin's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Validates a given password against the stored hash."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Admin {self.id}: {self.username}>'


class Organizer(db.Model, SerializerMixin):
    """
    Organizer Model: Represents an organization that hosts volunteer-driven events.
    
    Relationships:
    - One-to-Many with Events: An Organizer can host multiple events.
    """

    __tablename__ = 'organizers'
    serialize_rules = ('-events.organizer',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    contact_name = db.Column(db.String(255), nullable=False)
    contact_phone = db.Column(db.String(20), nullable=False)
    contact_email = db.Column(db.String(120), nullable=False, unique=True)

    events = db.relationship('Event', back_populates='organizer', cascade='all, delete-orphan')

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


class Event(db.Model, SerializerMixin):
    """
    Event Model: Represents an event hosted by an organization.
    
    Relationships:
    - Many-to-One with Organizer: Each Event is associated with one Organizer.
    - One-to-Many with Tasks: An Event can have multiple Tasks.
    - Many-to-Many with Volunteers: Volunteers can participate in multiple Events.
    """

    __tablename__ = 'events'
    serialize_rules = ('-organizer.events', '-tasks.event', '-volunteers.events')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    organizer_id = db.Column(db.Integer, db.ForeignKey('organizers.id'), nullable=False)

    organizer = db.relationship('Organizer', back_populates='events')
    tasks = db.relationship('Task', back_populates='event', cascade='all, delete-orphan')
    volunteers = db.relationship('Volunteer', secondary='event_volunteers', back_populates='events')

    @validates('name', 'location')
    def validate_not_empty(self, key, value):
        """Ensures that the event name and location are not empty."""
        if not value.strip():
            raise ValueError(f'{key.capitalize()} cannot be empty')
        return value

    def __repr__(self):
        """Returns a string representation of an Event instance."""
        return f'<Event {self.id}: {self.name}>'


class Volunteer(db.Model, SerializerMixin):
    """
    Volunteer Model: Represents volunteers who participate in events.
    
    Relationships:
    - Many-to-Many with Events: A Volunteer can participate in multiple Events.
    - One-to-Many with Tasks: A Volunteer can be assigned multiple Tasks.
    """

    __tablename__ = 'volunteers'
    serialize_rules = ('-tasks.volunteer', '-events.volunteers')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False)

    events = db.relationship('Event', secondary='event_volunteers', back_populates='volunteers')
    tasks = db.relationship('Task', back_populates='volunteer', cascade='all, delete-orphan')

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


class Task(db.Model, SerializerMixin):
    """
    Task Model: Represents tasks assigned to volunteers within an event.
    
    Relationships:
    - Many-to-One with Event: A Task belongs to an Event.
    - Many-to-One with Volunteer: A Task is assigned to a Volunteer.
    """

    __tablename__ = 'tasks'
    serialize_rules = ('-event.tasks', '-volunteer.tasks')

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='pending')
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteers.id'), nullable=True)

    event = db.relationship('Event', back_populates='tasks')
    volunteer = db.relationship('Volunteer', back_populates='tasks')

    @validates('title', 'description', 'status')
    def validate_not_empty(self, key, value):
        """Ensures that title, description, and status are not empty."""
        if not value.strip():
            raise ValueError(f'{key.capitalize()} cannot be empty')
        return value

    def __repr__(self):
        """Returns a string representation of a Task instance."""
        return f'<Task {self.id}: {self.title}>'


event_volunteers = db.Table(
    'event_volunteers',
    db.Column('event_id', db.Integer, db.ForeignKey('events.id'), primary_key=True),
    db.Column('volunteer_id', db.Integer, db.ForeignKey('volunteers.id'), primary_key=True)
)