from models import db, Event

def get_all_events():
    return [event.serialize() for event in Event.query.all()], 200

def get_event_by_id(event_id):
    event = Event.query.get(event_id)
    if not event:
        return {"error": "Event not found"}, 404
    return event.serialize(), 200

def create_event(data):
    new_event = Event(
        name=data['name'],
        date=data['date'],
        location=data['location'],
        organizer_id=data['organizer_id']
    )
    db.session.add(new_event)
    db.session.commit()
    return new_event.serialize(), 201

def update_event(event_id, data):
    event = Event.query.get(event_id)
    if not event:
        return {"error": "Event not found"}, 404

    for key, value in data.items():
        setattr(event, key, value)
    
    db.session.commit()
    return event.serialize(), 200

def delete_event(event_id):
    event = Event.query.get(event_id)
    if not event:
        return {"error": "Event not found"}, 404

    db.session.delete(event)
    db.session.commit()
    return {"message": "Event deleted successfully"}, 200
