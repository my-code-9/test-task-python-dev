# Task Manager API

REST API for task management built with Django REST Framework.

## Features

- Create tasks
- Update tasks
- Delete tasks
- Assign tasks to other users
- Mark tasks as completed
- Add comments to tasks
- JWT authentication
- Swagger API documentation
- PostgreSQL integration
- Automated tests

---

## Tech Stack

- Python 3.13
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Swagger / OpenAPI
- flake8
- black

---

## Project Structure

```text
task-manager-api/
│
├── .venv/
│
├── task_manager_api/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── tasks/
│   ├── migrations/
│   │   └── __init__.py
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── templates/
│
├── .env
├── .flake8
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

---

## Installation

### Clone repository

```bash
git clone <repository-url>
cd task-manager-api
```

---

## Create virtual environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## PostgreSQL Setup

Create PostgreSQL database:

```sql
CREATE DATABASE task_manager_db;
```

---

## Environment Variables

Create `.env` file in project root:

```env
DB_NAME=task_manager_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

## Run Migrations

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

Application:

```text
http://127.0.0.1:8000/
```

Swagger Documentation:

```text
http://127.0.0.1:8000/api/docs/
```

Admin Panel:

```text
http://127.0.0.1:8000/admin/
```

---

## Authentication

JWT authentication is implemented using Simple JWT.

### Get Access Token

Endpoint:

```text
POST /api/token/
```

Request body:

```json
{
    "username": "admin",
    "password": "your_password"
}
```

Response:

```json
{
    "refresh": "refresh_token",
    "access": "access_token"
}
```

Use token:

```text
Authorization: Bearer access_token
```

---

## API Endpoints

### Tasks

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/tasks/` | Get all tasks |
| POST | `/api/tasks/` | Create task |
| GET | `/api/tasks/{id}/` | Get task details |
| PUT | `/api/tasks/{id}/` | Update task |
| PATCH | `/api/tasks/{id}/` | Partial update |
| DELETE | `/api/tasks/{id}/` | Delete task |
| POST | `/api/tasks/{id}/complete/` | Mark task completed |
| POST | `/api/tasks/{id}/add_comment/` | Add comment |

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/token/` | Obtain JWT token |
| POST | `/api/token/refresh/` | Refresh JWT token |

---

## Example Create Task Request

```json
{
    "title": "Build Django API",
    "description": "Create task management backend",
    "status": "todo"
}
```

---

## Example Add Comment Request

```json
{
    "text": "Task completed successfully"
}
```

---

## Run Tests

```bash
python manage.py test
```

---

## Code Quality

The project follows:
- PEP 8 standards
- Django best practices
- REST API best practices
- Clean code principles
- Separation of concerns

### Run flake8

```bash
flake8
```

### Run black formatter

```bash
black .
```

### .flake8 Configuration

Create `.flake8`

```ini
[flake8]
max-line-length = 88
exclude =
    .venv,
    migrations,
    __pycache__
```

---

## Main Functionality Implemented

- Task creation
- Task editing
- Task deletion
- Task assignment to users
- Task completion
- Task comments
- JWT authorization
- Swagger API documentation
- PostgreSQL persistence
- Automated API tests

---

## Future Improvements

Possible future enhancements:

- Docker support
- CI/CD pipeline
- Pagination
- Filtering and search
- Email notifications
- User registration endpoint
- Celery background jobs

---

## Author

Python Django REST Framework Test Assignment - Renato Jr