# Task Manager API

REST API for task management built with Django REST Framework.

## Features

- JWT authentication
- Create, update, delete tasks
- Assign tasks to users
- Mark tasks as completed
- Add comments to tasks
- Swagger API documentation
- PostgreSQL database
- Automated tests

## Tech Stack

- Python 3.13
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Swagger

## Installation

### Clone repository

```bash
git clone <repo-url>
cd task-manager-api
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure PostgreSQL

Create PostgreSQL database:

```sql
CREATE DATABASE task_manager_db;
```

### Configure environment variables

Create `.env`

```env
DB_NAME=task_manager_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### Run migrations

```bash
python manage.py migrate
```

### Create superuser

```bash
python manage.py createsuperuser
```

### Run server

```bash
python manage.py runserver
```

## Swagger API Documentation

```text
http://127.0.0.1:8000/api/docs/
```

## Run Tests

```bash
python manage.py test
```