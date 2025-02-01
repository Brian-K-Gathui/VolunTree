# VolunTree 🌳 - Full Stack Application Project

## Author
**Brian Kinyanjui Gathui**  
📧 [briankgathui@gmail.com](mailto:briankgathui@gmail.com)

---

## Project Description
**VolunTree** is a robust platform designed to empower Organizations in creating and managing volunteer-driven charity events with ease and efficiency. VolunTree streamlines the entire process, taking care of everything—from **Organization Registration & Management** and **Volunteer Registration & Management** to **Event Creation & Management** and **Task Assignment & Management**—all with consultation from the organizations. By partnering with VolunTree, organizations can focus entirely on their mission while we handle the logistics, supported by our comprehensive suite of tools and dedicated team to ensure every event is executed flawlessly.

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

## 📂 Entities & Relationships

### Organizers
- `id` (Primary Key)
- `name` (Organization Name)
- `contact_name` (Main Contact)
- `contact_phone`
- `contact_email`
- **Relationships:** One-to-Many with **Event**

### Events
- `id` (Primary Key)
- `name`
- `date`
- `location`
- `organization_id` (Foreign Key referencing **Organizers**)
- **Relationships:**
  - Many-to-One with **Organizers**
  - One-to-Many with **Task**
  - Many-to-Many with **Volunteer**

### Volunteers
- `id` (Primary Key)
- `name`
- `email`
- `phone`
- **Relationships:** Many-to-Many with **Event**, One-to-Many with **Task**

### Tasks
- `id` (Primary Key)
- `title`
- `description`
- `status` ("pending", "in progress", "completed")
- `event_id` (Foreign Key referencing **Event**)
- `volunteer_id` (Foreign Key referencing **Volunteer**)
- **Relationships:** Many-to-One with **Event**, Many-to-One with **Volunteer**

---

## 🔗 Relationships Table

| Entity A    | Relationship Type | Entity B    | Description |
|------------|------------------|------------|-------------|
| Organizers | One-to-Many      | Event      | An Organizer can host multiple Events. |
| Event      | Many-to-One      | Organizers | An Event belongs to one Organizer. |
| Event      | One-to-Many      | Task       | An Event can have multiple Tasks. |
| Event      | Many-to-Many     | Volunteer  | An Event can have many Volunteers. |
| Volunteer  | Many-to-Many     | Event      | A Volunteer can join multiple Events. |
| Volunteer  | One-to-Many      | Task       | A Volunteer can have multiple Tasks. |
| Task       | Many-to-One      | Event      | A Task belongs to one Event. |
| Task       | Many-to-One      | Volunteer  | A Task is assigned to one Volunteer. |

---

---

## 🛠️ Technologies Used

### **Frontend (Client)**
- **React.js** – Dynamic and responsive UI
- **React Router** – Client-side navigation
- **Formik & Yup** – Form handling and validation
- **CSS/Styled Components** – Modern interface design
- **Fetch API** – Handles API communication

### **Backend (Server)**
- **Flask** – Lightweight Python framework
- **Flask-RESTful** – REST API development
- **Flask-SQLAlchemy** – ORM for database handling
- **Flask-Migrate** – Database migration support
- **Flask-CORS** – API Cross-Origin support

### **Database**
- **SQLite** – Lightweight relational database
- **SQLAlchemy ORM** – Pythonic database interactions

### **Development & Deployment**
- **Pipenv** – Backend dependency management
- **npm** – Frontend package management
- **Render** – Cloud-based hosting
- **Git & GitHub** – Version control

---

## 📁 Project File Structure
The **VolunTree** project follows a structured directory setup, ensuring clean separation of concerns between the frontend and backend components.

```plaintext
voluntree/
│── client/              # React Frontend
│   ├── README.md
│   ├── package.json     # Dependencies & Scripts
│   ├── public/          # Static assets
│   └── src/             # Source code
│       ├── components/  # UI components
│       ├── pages/       # App pages
│       ├── context/     # State management
│       ├── hooks/       # Custom hooks
│       ├── services/    # API requests
│       ├── styles/      # Global styles
│       ├── App.js       # Main App component
│       └── index.js     # Entry point
│
│── server/             # Flask Backend
│   ├── app.py          # Main Application
│   ├── config.py       # Configurations
│   ├── models.py       # Database models
│   ├── seed.py         # Database seeding
│   ├── migrations/     # Database migrations
│   ├── routes/         # API endpoints
│   ├── controllers/    # Business logic
│   ├── services/       # Helper functions
│   └── __init__.py     # Initialization
│
│── Pipfile             # Backend dependency manager
│── LICENSE.md          # License information
│── README.md           # Project documentation
│── .gitignore          # Git ignored files
│── .env                # Environment variables
```

<br><br>

---
## 📜 License

**MIT License** 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

Copyright © 2025 Brian Kinyanjui Gathui
