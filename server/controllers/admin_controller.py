from models import db, Admin

def get_all_admins():
    """Fetch all admins from the database."""
    return Admin.query.all()

def get_admin_by_id(admin_id):
    """Retrieve a single admin by ID."""
    return Admin.query.get(admin_id)

def create_admin(data):
    """Register a new admin."""
    if Admin.query.filter_by(username=data['username']).first():
        return {"error": "Username already exists"}, 400
    if Admin.query.filter_by(email=data['email']).first():
        return {"error": "Email already registered"}, 400
    
    new_admin = Admin(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        username=data['username']
    )
    new_admin.set_password(data['password'])
    
    db.session.add(new_admin)
    db.session.commit()
    return new_admin

def update_admin(admin_id, data):
    """Update an existing admin."""
    admin = Admin.query.get(admin_id)
    if not admin:
        return {"error": "Admin not found"}, 404
    
    for key, value in data.items():
        if key == 'password':
            admin.set_password(value)
        else:
            setattr(admin, key, value)
    
    db.session.commit()
    return admin

def delete_admin(admin_id):
    """Delete an admin from the database."""
    admin = Admin.query.get(admin_id)
    if not admin:
        return {"error": "Admin not found"}, 404
    
    db.session.delete(admin)
    db.session.commit()
    return {"message": "Admin deleted successfully"}, 200
