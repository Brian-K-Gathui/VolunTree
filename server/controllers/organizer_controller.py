from models import db, Organizer

def get_all_organizers():
    return Organizer.query.all()

def get_organizer_by_id(organizer_id):
    return Organizer.query.get(organizer_id)

def create_organizer(data):
    new_organizer = Organizer(
        name=data['name'],
        contact_name=data['contact_name'],
        contact_phone=data['contact_phone'],
        contact_email=data['contact_email']
    )
    db.session.add(new_organizer)
    db.session.commit()
    return new_organizer

def update_organizer(organizer_id, data):
    organizer = Organizer.query.get(organizer_id)
    if organizer:
        for key, value in data.items():
            setattr(organizer, key, value)
        db.session.commit()
    return organizer

def delete_organizer(organizer_id):
    organizer = Organizer.query.get(organizer_id)
    if organizer:
        db.session.delete(organizer)
        db.session.commit()
        return True
    return False
