from models import db, Organizer

def get_all_organizers():
    return [org.serialize() for org in Organizer.query.all()], 200

def get_organizer_by_id(organizer_id):
    organizer = Organizer.query.get(organizer_id)
    if not organizer:
        return {"error": "Organizer not found"}, 404
    return organizer.serialize(), 200

def create_organizer(data):
    new_organizer = Organizer(
        name=data['name'],
        contact_name=data['contact_name'],
        contact_phone=data['contact_phone'],
        contact_email=data['contact_email']
    )
    db.session.add(new_organizer)
    db.session.commit()
    return new_organizer.serialize(), 201

def update_organizer(organizer_id, data):
    organizer = Organizer.query.get(organizer_id)
    if not organizer:
        return {"error": "Organizer not found"}, 404

    for key, value in data.items():
        setattr(organizer, key, value)
    
    db.session.commit()
    return organizer.serialize(), 200

def delete_organizer(organizer_id):
    organizer = Organizer.query.get(organizer_id)
    if not organizer:
        return {"error": "Organizer not found"}, 404

    db.session.delete(organizer)
    db.session.commit()
    return {"message": "Organizer deleted successfully"}, 200
