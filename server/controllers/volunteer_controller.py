from models import db, Volunteer

def get_all_volunteers():
    """Fetch all volunteers from the database."""
    return [vol.serialize() for vol in Volunteer.query.all()], 200

def get_volunteer_by_id(volunteer_id):
    """Retrieve a single volunteer by ID."""
    volunteer = Volunteer.query.get(volunteer_id)
    if not volunteer:
        return {"error": "Volunteer not found"}, 404
    return volunteer.serialize(), 200

def create_volunteer(data):
    """Register a new volunteer."""
    new_volunteer = Volunteer(
        name=data['name'],
        email=data['email'],
        phone=data['phone']
    )
    db.session.add(new_volunteer)
    db.session.commit()
    return new_volunteer.serialize(), 201

def update_volunteer(volunteer_id, data):
    """Update an existing volunteer."""
    volunteer = Volunteer.query.get(volunteer_id)
    if not volunteer:
        return {"error": "Volunteer not found"}, 404

    for key, value in data.items():
        setattr(volunteer, key, value)
    
    db.session.commit()
    return volunteer.serialize(), 200

def delete_volunteer(volunteer_id):
    """Delete a volunteer from the database."""
    volunteer = Volunteer.query.get(volunteer_id)
    if not volunteer:
        return {"error": "Volunteer not found"}, 404

    db.session.delete(volunteer)
    db.session.commit()
    return {"message": "Volunteer deleted successfully"}, 200
