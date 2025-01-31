# VolunTree 🌳 - Full Stack Application Project

**Author:** Brian Kinyanjui Gathui  
**Email:** [briankgathui@gmail.com](mailto:briankgathui@gmail.com)
<br><br>

## Project Description
**VolunTree** is a robust platform designed to empower Organizations in creating and managing volunteer-driven charity events with ease and efficiency. VolunTree streamlines the entire process, taking care of everything—from **Organization Registration & Management** and **Volunteer Registration & Management** to **Event Creation & Management** and **Task Assignment & Management**—all with consultation from the organizations. By partnering with VolunTree, organizations can focus entirely on their mission while we handle the logistics, supported by our comprehensive suite of tools and dedicated team to ensure every event is executed flawlessly.

<br>

## Key Features:
The following table outlines the core functionalities of **VolunTree**, highlighting how the platform efficiently manages organizations, volunteers, events, and tasks. Each feature is designed to streamline operations, ensuring smooth execution of volunteer-driven charity events with minimal effort from organizations.
| #  | **Feature**                         | **Description** |
|----|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | **Staff-Managed Platform**           | Every aspect of the platform—from registration to task management—is exclusively managed by VolunTree staff. This ensures precision, care, and seamless execution, allowing organizations and volunteers to focus on making a meaningful impact without logistical worries. |
| 2  | **Organization Registration & Management** | **Registration:** VolunTree staff manage the entire registration process for organizations, collecting essential details such as organization name, contact person, phone number, and email address. <br><br> **Management:** Our team ensures all organization information is accurate and up-to-date, while also assisting in setting up and managing multiple events under a single account. |
| 3  | **Volunteer Registration & Management** | **Registration:** Volunteers can easily sign up through VolunTree, with staff managing the process to create detailed profiles that highlight interests and availability. <br><br> **Management:** Our team matches volunteers to events, maintains communication, and ensures a seamless experience for both volunteers and organizations. |
| 4  | **Event Creation & Management**      | **Creation:** VolunTree staff work closely with organizations to create events, capturing details like event name, date, location, and specific objectives. <br><br> **Management:** From planning to execution, our team oversees every aspect of the event, ensuring smooth logistics, volunteer coordination, and timely completion. |
| 5  | **Task Assignment & Management**     | **Assignment:** VolunTree staff assist organizations in assigning tasks to volunteers, ensuring clear roles and responsibilities. Tasks are tracked with statuses like "pending," "in progress," and "completed." <br> **Management:** Our team monitors task progress, provides support to volunteers, and resolves any issues to keep events on track. |
| 6  | **Comprehensive Entity Management**  | VolunTree staff manage all key entities and their relationships through a centralized system: <br> **Organizations:** Can host multiple events, each with its own tasks and volunteers. <br> **Events:** Linked to one organizer, with multiple volunteers and tasks. <br> **Volunteers:** Can participate in multiple events and handle various tasks. <br> **Tasks:** Assigned to individual volunteers and tied to specific events. |

VolunTree streamlines the entire process, allowing organizations to focus on their mission while we handle the logistics. By partnering with VolunTree, organizations outsource their volunteer-driven charity events to VolunTree, and VolunTree leverages its comprehensive suite of tools to execute these events seamlessly. 
Together, we foster a collaborative environment where organizations can efficiently manage their charity events, and volunteers can engage in meaningful roles, all supported by our committed staff. With VolunTree, organizations can trust that every event will be executed flawlessly, allowing them to achieve their goals without the operational burden.

<br>

## Entities & Relationships


| **Organizers** | **Event** |
|--------------|--------|
| **Attributes:** <br> - `id` (primary key) <br> - `name` (e.g., the company’s or group’s name) <br> - `contact_name` (the main contact’s name) <br> - `contact_phone` <br> - `contact_email` <br> **Relationships:** <br> - One-to-many with **Event** (an Organizer can host many Events) | **Attributes:** <br> - `id` (primary key) <br> - `name` <br> - `date` <br> - `location` <br> - `organization_id` (foreign key referencing **Organizers**) <br> **Relationships:** <br> - Many-to-one with **Organizers** (an Event is hosted by exactly one Organizer) <br> - One-to-many with **Task** (an Event can have many Tasks) <br> - Many-to-many with **Volunteer** (an Event can have many Volunteers, and a Volunteer can join many Events) |

| **Volunteer** | **Task** |
|--------------|--------|
| **Attributes:** <br> - `id` (primary key) <br> - `name` <br> - `email` <br> - `phone` <br> **Relationships:** <br> - One-to-many with **Task** (one Volunteer can have many Tasks) <br> - Many-to-many with **Event** | **Attributes:** <br> - `id` (primary key) <br> - `title` <br> - `description` <br> - `status` (e.g., "pending", "in progress", "completed") <br> - `event_id` (foreign key referencing **Event**) <br> - `volunteer_id` (foreign key referencing **Volunteer**) <br> **Relationships:** <br> - Many-to-one with **Event** (a Task belongs to exactly one Event) <br> - Many-to-one with **Volunteer** (a Task can be assigned to exactly one Volunteer) |

This grid ensures all the attributes and relationships for each entity are neatly organized within each table cell. Let me know if you need any adjustments! 🚀



## Relationships Table

| Entity A    | Relationship Type | Entity B    | Description |
|------------|------------------|------------|-------------|
| Organizers | One-to-Many      | Event      | An Organizer can host multiple Events, but an Event belongs to one Organizer. |
| Event      | Many-to-One      | Organizers | An Event is hosted by one Organizer. |
| Event      | One-to-Many      | Task       | An Event can have multiple Tasks, but a Task belongs to one Event. |
| Event      | Many-to-Many     | Volunteer  | An Event can have many Volunteers, and a Volunteer can join multiple Events. |
| Volunteer  | Many-to-Many     | Event      | A Volunteer can join multiple Events, and an Event can have multiple Volunteers. |
| Volunteer  | One-to-Many      | Task       | A Volunteer can have multiple Tasks, but a Task is assigned to only one Volunteer. |
| Task       | Many-to-One      | Event      | A Task belongs to one Event. |
| Task       | Many-to-One      | Volunteer  | A Task is assigned to one Volunteer. |

<br>

## Technologies Used
The **VolunTree** platform is built using a modern full-stack approach, integrating a powerful backend with an interactive frontend for seamless user experience. The following technologies and frameworks were utilized:
### **Frontend (Client)**
- **React.js** – Frontend JavaScript framework for building a dynamic and responsive UI.
- **React Router** – Enables client-side routing for seamless navigation.
- **Formik & Yup** – Used for form handling and validation.
- **CSS/Styled Components** – Styling for a clean and modern interface.
- **Fetch API** – Handles communication with the backend API.

### **Backend (Server)**
- **Flask** – Lightweight Python framework used for the backend API.
- **Flask-RESTful** – Facilitates building RESTful APIs.
- **Flask-SQLAlchemy** – ORM for handling database operations.
- **Flask-Migrate** – Handles database migrations.
- **Flask-CORS** – Enables Cross-Origin Resource Sharing for API requests.

### **Database**
- **SQLite** – Lightweight relational database for data storage.
- **SQLAlchemy ORM** – Used to interact with the database using Python objects.

### **Development & Deployment**
- **Pipenv** – Dependency management for the backend.
- **npm** – Package manager for frontend dependencies.
- **Render** – Deployment platform for hosting the application.
- **Git & GitHub** – Version control and collaboration.

<br>

## Project File Structure
The **VolunTree** project follows a structured directory setup, ensuring clean separation of concerns between the frontend and backend components.

```plaintext
voluntree/
│── client/              # React Frontend
│   ├── README.md
│   ├── package.json     # Dependencies & Scripts
│   ├── public/          # Static assets
│   └── src/             # Source code for React app
│       ├── components/  # Reusable UI components
│       ├── pages/       # Application pages
│       ├── context/     # Global state management
│       ├── hooks/       # Custom hooks
│       ├── services/    # API request handling
│       ├── styles/      # Global styles & themes
│       ├── App.js       # Main App component
│       └── index.js     # React entry point
│
│── server/             # Flask Backend
│   ├── app.py          # Flask Application
│   ├── config.py       # Configuration settings
│   ├── models.py       # Database models
│   ├── seed.py         # Database seeding script
│   ├── migrations/     # Database migrations
│   ├── instance/       # SQLite database storage
│   ├── routes/         # API endpoints
│   ├── controllers/    # Business logic
│   ├── services/       # Helper functions
│   └── __init__.py     # App initialization
│
│── Pipfile             # Backend dependency manager
│── LICENSE.md          # License information
│── README.md           # Project documentation
│── .gitignore          # Files to ignore in version control
│── .env                # Environment variables (ignored in Git)
```
<br>


<br><br>

## License

MIT License  

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

Copyright © 2025 Brian Kinyanjui Gathui
