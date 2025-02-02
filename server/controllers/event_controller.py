from models import db, Event

def get_all_events():
    """Fetch all events from the database."""
    return Event.query.all()

def get_event_by_id(event_id):
    """Retrieve a single event by ID."""
    return Event.query.get(event_id)

def create_event(data):
    """Create a new event."""
    new_event = Event(
        name=data['name'],
        date=data['date'],
        location=data['location'],
        organizer_id=data['organizer_id']
    )
    db.session.add(new_event)
    db.session.commit()
    return new_event

def update_event(event_id, data):
    """Update an existing event."""
    event = Event.query.get(event_id)
    if event:
        for key, value in data.items():
            setattr(event, key, value)
        db.session.commit()
    return event

def delete_event(event_id):
    """Delete an event from the database."""
    event = Event.query.get(event_id)
    if event:
        db.session.delete(event)
        db.session.commit()
        return True
    return False
