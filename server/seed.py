#!/usr/bin/env python3

# ===============================
#         SEED SCRIPT
# ===============================

# Standard library imports
from random import randint, choice as rc  # Random selection and number generation

# Remote library imports
from faker import Faker  # Faker generates realistic fake data

# Local imports
from app import app  # Importing the Flask application instance
from models import db, Organizer, Event, Volunteer, Task, event_volunteers  # Importing models

# Instantiate Faker
fake = Faker()

if __name__ == '__main__':
    with app.app_context():  # Ensures database operations are executed in the app's context
        print("Starting seed process...")

        # ===============================
        # DELETE EXISTING DATABASE DATA
        # ===============================

        print("Clearing old data...")
        db.session.query(event_volunteers).delete()  # Clear event-volunteers association table first
        db.session.query(Task).delete()  # Clear tasks
        db.session.query(Event).delete()  # Clear events
        db.session.query(Volunteer).delete()  # Clear volunteers
        db.session.query(Organizer).delete()  # Clear organizers

        # Commit deletion
        db.session.commit()
        print("Old data cleared!")

        # ===============================
        # SEED ORGANIZERS
        # ===============================

        print("Seeding organizers...")
        organizers = []
        for _ in range(5):  # Creating 5 organizations
            organizer = Organizer(
                name=fake.company(),
                contact_name=fake.name(),
                contact_phone=fake.phone_number(),
                contact_email=fake.email()
            )
            organizers.append(organizer)

        # Bulk insert organizers into the database
        db.session.add_all(organizers)
        db.session.commit()
        print(f"Seeded {len(organizers)} organizers!")

        # ===============================
        # SEED EVENTS
        # ===============================

        print("Seeding events...")
        events = []
        for _ in range(10):  # Creating 10 events
            event = Event(
                name=fake.catch_phrase(),  # Generates a random event name
                date=fake.date_between(start_date='-1y', end_date='+1y'),  # Random date within a year
                location=fake.city(),
                organizer_id=rc([org.id for org in organizers])  # Randomly assign an organizer
            )
            events.append(event)

        db.session.add_all(events)
        db.session.commit()
        print(f"Seeded {len(events)} events!")

        # ===============================
        # SEED VOLUNTEERS
        # ===============================

        print("Seeding volunteers...")
        volunteers = []
        for _ in range(15):  # Creating 15 volunteers
            volunteer = Volunteer(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number()
            )
            volunteers.append(volunteer)

        db.session.add_all(volunteers)
        db.session.commit()
        print(f"Seeded {len(volunteers)} volunteers!")

        # ===============================
        # SEED EVENT-VOLUNTEERS ASSOCIATION
        # ===============================

        print("Assigning volunteers to events...")
        event_volunteer_entries = []
        for volunteer in volunteers:
            assigned_events = rc(events, randint(1, 3))  # Each volunteer is assigned 1-3 events
            for event in assigned_events:
                event_volunteer_entries.append(
                    {"event_id": event.id, "volunteer_id": volunteer.id}
                )

        # Execute bulk insert for event-volunteers many-to-many association
        db.session.execute(event_volunteers.insert(), event_volunteer_entries)
        db.session.commit()
        print(f"Assigned volunteers to {len(event_volunteer_entries)} event-volunteer entries!")

        # ===============================
        # SEED TASKS
        # ===============================

        print("Seeding tasks...")
        statuses = ["pending", "in progress", "completed"]
        tasks = []
        for _ in range(20):  # Creating 20 tasks
            task = Task(
                title=fake.sentence(nb_words=5),  # Generates a random task title
                description=fake.text(),  # Generates a random task description
                status=rc(statuses),  # Randomly assign a status
                event_id=rc([event.id for event in events]),  # Assign task to a random event
                volunteer_id=rc([vol.id for vol in volunteers]) if randint(0, 1) else None  # Assign to a volunteer randomly
            )
            tasks.append(task)

        db.session.add_all(tasks)
        db.session.commit()
        print(f"Seeded {len(tasks)} tasks!")

        # ===============================
        # COMPLETION MESSAGE
        # ===============================
        print("Seeding process completed successfully!")
