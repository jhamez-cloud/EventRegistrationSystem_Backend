# Event Registration System - Backend API & Admin Panel

A scalable backend API and administrative management system for creating, managing, and monitoring events. Built with **Django** and **Django REST Framework**, the project provides secure RESTful APIs, role-based administration, event management, registration tracking, and content management through the Django Admin interface.

---

## Features

### Authentication & User Management

* Custom User Model
* JWT Authentication
* User Registration & Login
* Role-based Access Control
* User Profile Management

### Event Management

* Create, Update, Delete and View Events
* Event Categories
* Event Slugs
* Event Status Management
* Free and Paid Events
* Event Capacity Tracking
* Registration Count

### Event Details

Each event can include:

* Detailed Description
* Event Venue
* Organizers
* Speakers
* Agenda/Schedule
* Gallery Images
* Event Tags

### Registration Management

* Event Registration
* Registration Status Tracking
* Capacity Validation
* Attendee Management

### Admin Panel

A fully customized Django Admin interface for managing:

* Users
* Events
* Event Details
* Speakers
* Organizers
* Venues
* Agenda Items
* Tags
* Gallery Images
* Registrations

### REST API

RESTful endpoints for:

* Authentication
* Users
* Events
* Event Details
* Event Registration
* Categories
* Supporting Resources

---

# Tech Stack

| Technology            | Purpose                  |
| --------------------- | ------------------------ |
| Python 3              | Programming Language     |
| Django                | Web Framework            |
| Django REST Framework | REST API Development     |
| Simple JWT            | Authentication           |
| SQLite / PostgreSQL   | Database                 |
| Pillow                | Image Upload Handling    |
| Django Admin          | Administrative Dashboard |
| RESTful API           | Client Communication     |

---

# Project Structure

```text
EventRegistrationSystem_Backend/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── user/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── admin.py
│
├── event/
│   ├── models.py
│   ├── serializers.py
│   ├── viewsets.py
│   ├── urls.py
│   └── admin.py
│
├── media/
├── requirements.txt
├── manage.py
└── README.md
```

---

# Database Relationships

```
EventList
    │
    └── One-to-One
            │
       EventDetail
            │
            ├── Venue
            ├── Organizers
            ├── Speakers
            ├── Agenda
            ├── Gallery
            └── Tags
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/EventRegistrationSystem_Backend.git

cd EventRegistrationSystem_Backend
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Apply Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

## Run Development Server

```bash
python manage.py runserver
```

Server will be available at:

```
http://127.0.0.1:8000/
```

---

# Authentication

The API uses **JWT Authentication**.

Typical authentication flow:

1. Register User
2. Login
3. Receive:

```json
{
    "access": "...",
    "refresh": "..."
}
```

4. Include the access token in subsequent requests:

```
Authorization: Bearer <access_token>
```

---

# API Endpoints

## Authentication

```
POST    /api/auth/register/
POST    /api/auth/login/
POST    /api/auth/refresh/
```

---

## Events

```
GET     /api/v1/events/
POST    /api/v1/events/

GET     /api/v1/events/{id}/
PUT     /api/v1/events/{id}/
PATCH   /api/v1/events/{id}/
DELETE  /api/v1/events/{id}/
```

---

## Event Details

```
GET     /api/v1/event-detail/
POST    /api/v1/event-detail/

GET     /api/v1/event-detail/{id}/
PUT     /api/v1/event-detail/{id}/
PATCH   /api/v1/event-detail/{id}/
DELETE  /api/v1/event-detail/{id}/
```

---

## Registration

```
POST    /api/v1/register/
GET     /api/v1/register/
```

---

# Media Uploads

The API supports media uploads for:

* Event Thumbnails
* Gallery Images
* Speaker Photos

Media files are stored in:

```
media/
```

---

# Validation

The backend includes validation for:

* Event Capacity
* Required Fields
* Event Status
* Duplicate Records
* Slug Generation
* Image Uploads
* Relationship Integrity

---

# API Testing

Recommended tools:

* Postman
* Insomnia
* Bruno
* Thunder Client (VS Code)

---

# Future Improvements

* Email Notifications
* QR Code Ticket Generation
* Event Check-in
* Payment Gateway Integration
* Event Analytics Dashboard
* Search & Filtering
* Event Reviews
* Wishlists
* Social Authentication
* Docker Deployment
* CI/CD Pipeline
* API Documentation (Swagger/OpenAPI)

---

# Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit changes

```bash
git commit -m "Add new feature"
```

4. Push the branch

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

# Author

**James Kekeli**

Backend Developer

* Django
* Django REST Framework
* REST API Development
* Python
* PostgreSQL
* JWT Authentication
* Backend System Design

If you found this project useful, consider giving it a ⭐ on GitHub!
