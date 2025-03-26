# Task Management API

## Project Overview
Task Management API is a Django-based web application that provides robust task management functionality. The application allows users to create, assign, and track tasks with various statuses and types.

## Features

- **User Management**
  - Create and manage user accounts
  - Custom user model with mobile number support
- **CRUD operations for tasks**
  - Create tasks with detailed information
  - Assign tasks to multiple users
  - Status tracking with automatic completion timestamps (Pending, In Progress, Completed)
  - Multiple task types (Personal, Work, Shopping, Other)
- RESTful API endpoints
- Interactive Swagger documentation
- Admin dashboard for management

## Installation Setup
1. Clone the repository
```bash
git clone <repository-url>
cd task_management_api
```
2. Create a virtual environment and activate it:
```bash
python -m venv venv
`venv\Scripts\activate`# On linux or MacOs  use venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Create a superuser:
```bash
python manage.py createsuperuser
```
6. Run the development server:
```bash
python manage.py runserver
```

## 📌 USER ENDPOINTS
### 🔹 Create a User  
**Endpoint:** `POST /api/users/`  

#### **Request:**
```json
{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword",
    "mobile": "+1234567890"
}
```

#### **Response:**
```json
{
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "mobile": "+1234567890"
}
```

### 🔹 List all users 
**Endpoint:** `GET /api/users/`

### 🔹 Retrieve a User with details about task.
**Endpoint:** `GET /api/users/<id>/`

## 📌 TASK ENDPOINTS

### 🔹 List all tasks 
**Endpoint:** `GET /api/tasks/`

### 🔹 Post a task
**Endpoint:** `POST /api/tasks/`
```json
{
    "name": "Implement auth system",
    "description": "Add JWT authentication to API endpoints",
    "task_type": "WORK",
    "assigned_users_ids": [1]
}
```
### Mark task as completed

#### **Request:**
```json
{
    "status": "COMPLETED"
}
```

#### **Response:**
```json
{
    "id": 1,
    "name": "Implement auth system",
    "description: "Add JWT authentication to API endpoints",
    "created_at": "2025-03-25T14:28:00Z"  # auto added
    "status": "COMPLETED",
    "completed_at": "2025-03-25T14:30:00Z", # auto updated when status changes to "COMPLETED"
    "assigned_users": [1]
}
```

### 🔹 Assign a task to  user/users 
**Endpoint:** `POST /api/tasks/<id>/assign_users/`
```json
{
    "assigned_users_ids": [1, 2, 3]
}
```
### 🔹 Retrieving a task of a specific user
**Endpoint:** `GET /api/tasks/user/<user_id>/`

## API Documentation
#### **Access the interactive API documentation:**
- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/

** More features such as authentication and authorization can be implemented as per project requirements **
