import random
from random import randint, choice as rc
from faker import Faker
from werkzeug.security import generate_password_hash

from app import app
from models import db, Organizer, Event, Volunteer, Task, event_volunteers, Admin

fake = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("🚀 Starting seed process...")
        print("_____________________________________________\n")

        # Clearing old data
        print("_____________________________________________\n")
        print("🗑️  Clearing old data...")
        db.session.query(event_volunteers).delete()
        db.session.query(Task).delete()
        db.session.query(Event).delete()
        db.session.query(Volunteer).delete()
        db.session.query(Organizer).delete()
        db.session.query(Admin).delete()
        db.session.commit()
        print("✅ Old data cleared!")
        print("_____________________________________________\n")

        # Seeding Admins
        print("_____________________________________________\n")
        print("👨‍💼 Seeding admin users...")
        admin_users = [
            Admin(
                first_name="Brian",
                last_name="Gathui",
                email="brian.gathui@gmail.com",
                username="brian_admin",
                password_hash=generate_password_hash("admin123")
            ),
            Admin(
                first_name="Alice",
                last_name="Johnson",
                email="alice.johnson@gmail.com",
                username="alice_admin",
                password_hash=generate_password_hash("securePass!")
            ),
            Admin(
                first_name="Michael",
                last_name="Smith",
                email="michael.smith@gmail.com",
                username="mike_admin",
                password_hash=generate_password_hash("michael2024")
            )
        ]
        db.session.add_all(admin_users)
        db.session.commit()
        print(f"✅ Seeded {len(admin_users)} admin users!")
        print("_____________________________________________\n")

        # Seeding Organizers
        print("_____________________________________________\n")
        print("🏢 Seeding organizers...")
        organizers = []
        for _ in range(5):
            organizer = Organizer(
                name=fake.company(),
                contact_name=fake.name(),
                contact_phone=fake.phone_number(),
                contact_email=fake.email()
            )
            organizers.append(organizer)
        db.session.add_all(organizers)
        db.session.commit()
        print(f"✅ Seeded {len(organizers)} organizers!")
        print("_____________________________________________\n")

        # Seeding Events
        print("📅 Seeding events...")
        events = []
        for _ in range(10):
            event = Event(
                name=fake.catch_phrase(),
                date=fake.date_between(start_date='-1y', end_date='+1y'),
                location=fake.city(),
                organizer_id=rc([org.id for org in organizers])
            )
            events.append(event)
        db.session.add_all(events)
        db.session.commit()
        print(f"✅ Seeded {len(events)} events!")
        print("_____________________________________________\n")

        # Seeding Volunteers
        print("🙋 Seeding volunteers...")
        volunteers = []
        for _ in range(15):
            volunteer = Volunteer(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number()
            )
            volunteers.append(volunteer)
        db.session.add_all(volunteers)
        db.session.commit()
        print(f"✅ Seeded {len(volunteers)} volunteers!")
        print("_____________________________________________\n")

        # Assigning Volunteers to Events
        print("🔗 Assigning volunteers to events...")
        event_volunteer_entries = []
        for volunteer in volunteers:
            assigned_events = random.sample(events, randint(1, min(3, len(events))))
            for event in assigned_events:
                event_volunteer_entries.append(
                    {"event_id": event.id, "volunteer_id": volunteer.id}
                )
        db.session.execute(event_volunteers.insert(), event_volunteer_entries)
        db.session.commit()
        print(f"✅ Assigned volunteers to {len(event_volunteer_entries)} event-volunteer entries!")
        print("_____________________________________________\n")

        # Seeding Tasks
        print("📝 Seeding tasks...")
        statuses = ["pending", "in progress", "completed"]
        tasks = []
        for _ in range(20):
            task = Task(
                title=fake.sentence(nb_words=5),
                description=fake.text(),
                status=rc(statuses),
                event_id=rc([event.id for event in events]),
                volunteer_id=rc([vol.id for vol in volunteers]) if randint(0, 1) else None
            )
            tasks.append(task)
        db.session.add_all(tasks)
        db.session.commit()
        print(f"✅ Seeded {len(tasks)} tasks!")
        print("_____________________________________________\n")

        print("🎉 SEEDING PROCESS COMPLETED SUCCESSFULLY! 🚀")
        print("_____________________________________________\n")
