# Task Management API

This project is a RESTful API for a task management system, built using **Django** and **Django REST Framework (DRF)**. The API provides functionality to create tasks, assign them to users, and retrieve assigned tasks.

---

## Features

- Create a new task
- Assign tasks to one or multiple users
- Retrieve tasks assigned to a specific user

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/heyprincesingh/josh-talks.git
cd josh-talks
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Admin Access)

To manage users and tasks via the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to enter a username, email, and password.

### 6. Create a Regular User or Admin Console

To create a regular user, use the Django shell:

```bash
python manage.py shell
```

Then run the following commands:

```python
from tasks.models import User
user = User.objects.create_user(username="heyprincesingh", email="princesingh3632@gmail.com", password="password123", mobile="7309233501")
user.save()
```

Exit the shell by typing:

```python
exit()
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

The API will be available at:  
**http://127.0.0.1:8000/**

---

## API Endpoints

### 1. Create a Task

**Endpoint:** `POST /api/tasks/create/`

**Hearder**: `Content-Type:application/json`

**Request Body:**
```json
{
    "name": "Finish Project",
    "description": "Complete the josh Talks' Django project",
    "task_type": "Assessment"
}
```
**Response:**
```json
{
    "id": 1,
    "name": "Finish Project",
    "description": "Complete the josh Talks' Django project",
    "task_type": "Assessment",
    "created_at": "2025-03-24T12:00:00Z",
    "status": "Pending",
    "assigned_users": []
}
```

---

### 2. Assign a Task to Users

**Endpoint:** `POST /api/tasks/assign/{task_id}/`  

**Hearder**: `Content-Type:application/json`

**Request Body:**
```json
{
    "assigned_users": [1, 2]
}
```
**Response:**
```json
{
    "message": "Task assigned successfully"
}
```

---

### 3. Get Tasks Assigned to a User

**Endpoint:** `GET /api/tasks/user/{user_id}/`  
**Response:**
```json
[
    {
        "id": 1,
        "name": "Finish Project",
        "description": "Complete the josh Talks' Django project",
        "task_type": "Assessment",
        "created_at": "2025-03-24T12:00:00Z",
        "status": "Pending",
        "assigned_users": [
            {
                "id": 1,
                "username": "heyprincesingh",
                "email": "princesingh3632@gmail.com",
                "mobile": "7309233501"
            }
        ]
    }
]
```

---
multiple users
- Retrieve tasks assigned to a specific user

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/heyprincesingh/josh-talks.git
cd josh-talks
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Admin Access)

To manage users and tasks via the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to enter a username, email, and password.

### 6. Create a Regular User or Admin Console

To create a regular user, use the Django shell:

```bash
python manage.py shell
```

Then run the following commands:

```python
from tasks.models import User
user = User.objects.create_user(username="heyprincesingh", email="princesingh3632@gmail.com", password="password123", mobile="7309233501")
user.save()
```

Exit the shell by typing:

```python
exit()
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

The API will be available at:  
**http://127.0.0.1:8000/**

---

## API Endpoints

### 1. Create a Task

**Endpoint:** `POST /api/tasks/create/`  
**Request Body:**
```json
{
    "name": "Finish Project",
    "description": "Complete the josh Talks' Django project",
    "task_type": "Assessment"
}
```
**Response:**
```json
{
    "id": 1,
    "name": "Finish Project",
    "description": "Complete the josh Talks' Django project",
    "task_type": "Assessment",
    "created_at": "2025-03-24T12:00:00Z",
    "status": "Pending",
    "assigned_users": []
}
```

---

### 2. Assign a Task to Users

**Endpoint:** `POST /api/tasks/assign/{task_id}/`  
**Request Body:**
```json
{
    "assigned_users": [1, 2]
}
```
**Response:**
```json
{
    "message": "Task assigned successfully"
}
```

---

### 3. Get Tasks Assigned to a User

**Endpoint:** `GET /api/tasks/user/{user_id}/`  
**Response:**
```json
[
    {
        "id": 1,
        "name": "Finish Project",
        "description": "Complete the josh Talks' Django project",
        "task_type": "Assessment",
        "created_at": "2025-03-24T12:00:00Z",
        "status": "Pending",
        "assigned_users": [
            {
                "id": 1,
                "username": "heyprincesingh",
                "email": "princesingh3632@gmail.com",
                "mobile": "7309233501"
            }
        ]
    }
]
```

---
