import random
from random import randint, choice as rc
from faker import Faker

from app import app
from models import db, Organizer, Event, Volunteer, Task, event_volunteers

fake = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("\n🚀 Starting seed process...")
        print("_____________________________________________\n")

        print("🗑️  Clearing old data...")
        db.session.query(event_volunteers).delete()
        db.session.query(Task).delete()
        db.session.query(Event).delete()
        db.session.query(Volunteer).delete()
        db.session.query(Organizer).delete()
        db.session.commit()
        print("✅ Old data cleared!")
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
