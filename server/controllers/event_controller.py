from models import db, Event

def get_all_events():
    return Event.query.all()

def get_event_by_id(event_id):
    return Event.query.get(event_id)

def create_event(data):
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
    event = Event.query.get(event_id)
    if event:
        for key, value in data.items():
            setattr(event, key, value)
        db.session.commit()
    return event

def delete_event(event_id):
    event = Event.query.get(event_id)
    if event:
        db.session.delete(event)
        db.session.commit()
        return True
    return False
