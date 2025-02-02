from models import db, Volunteer

def get_all_volunteers():
    """Fetch all volunteers from the database."""
    return Volunteer.query.all()

def get_volunteer_by_id(volunteer_id):
    """Retrieve a single volunteer by ID."""
    return Volunteer.query.get(volunteer_id)

def create_volunteer(data):
    """Register a new volunteer."""
    new_volunteer = Volunteer(
        name=data['name'],
        email=data['email'],
        phone=data['phone']
    )
    db.session.add(new_volunteer)
    db.session.commit()
    return new_volunteer

def update_volunteer(volunteer_id, data):
    """Update an existing volunteer."""
    volunteer = Volunteer.query.get(volunteer_id)
    if volunteer:
        for key, value in data.items():
            setattr(volunteer, key, value)
        db.session.commit()
    return volunteer

def delete_volunteer(volunteer_id):
    """Delete a volunteer from the database."""
    volunteer = Volunteer.query.get(volunteer_id)
    if volunteer:
        db.session.delete(volunteer)
        db.session.commit()
        return True
    return False
