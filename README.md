# Metall API

This project is a Django REST API for Metall. It is configured for both local development and production deployment.

## Features
- Django REST Framework API with function-based views
- Swagger and ReDoc documentation via drf-yasg at /swagger and /redoc
- Admin site at /admin
- Environment-driven settings (SECRET_KEY, DEBUG, ALLOWED_HOSTS, DB, etc.)
- Static files served by WhiteNoise in production
- Media files support (served by Django only in DEBUG)

## Requirements
- Python 3.10+
- pip

## Quick start (development)
```
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env  # edit if needed
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py runserver
```
Visit:
- API: http://127.0.0.1:8000/api/v1/
- Swagger: http://127.0.0.1:8000/swagger/
- Admin: http://127.0.0.1:8000/admin/

## Environment variables (.env)
This project uses django-environ and automatically loads a .env file from the project root. Copy .env.example to .env and adjust values.

Supported keys:
- DJANGO_SECRET_KEY: Strong secret key for production.
- DJANGO_DEBUG: "False" in production. Defaults to True.
- DJANGO_ALLOWED_HOSTS: Comma-separated hosts, e.g. "example.com,www.example.com". Defaults to "*".
- DJANGO_CSRF_TRUSTED_ORIGINS: Comma-separated origins, e.g. "https://example.com,https://www.example.com".
- DJANGO_DB_NAME: Database name (e.g., myproject).
- DJANGO_DB_USER: Database user (e.g., myprojectuser).
- DJANGO_DB_PASSWORD: Database password.
- DJANGO_DB_HOST: Database host (e.g., localhost).
- DJANGO_DB_PORT: Database port (leave empty for default 5432).
- DJANGO_SESSION_COOKIE_SECURE: Set to "True" if serving over HTTPS.
- DJANGO_CSRF_COOKIE_SECURE: Set to "True" if serving over HTTPS.
- DJANGO_SECURE_SSL_REDIRECT: Set to "True" to force HTTPS.
- DJANGO_SECURE_PROXY_SSL_HEADER: Set to "True" if behind a proxy that sets X-Forwarded-Proto.

Example:
```
cp .env.example .env
# then edit .env
```

### PostgreSQL configuration
Set the individual database settings in your .env, for example:
```
DJANGO_DB_NAME=myproject
DJANGO_DB_USER=myprojectuser
DJANGO_DB_PASSWORD=password
DJANGO_DB_HOST=localhost
DJANGO_DB_PORT=
```
Install requirements and run migrations:
```
pip install -r requirements.txt
python manage.py migrate
```

## Admin import/export
This project includes django-import-export. In the Django admin, each model supports CSV/XLSX import and export via the "Import" and "Export" actions on the changelist page.

## Mock data
Mock data is seeded via a Django data migration. After setting up the project (and database), simply run:
```
python manage.py migrate
```
The migration v1.0002_mock_data creates sample categories, products, banners, about-us entry, statistics, clients, and a lead. It uses placeholder file paths for image fields; files are not required to exist.

## Static and media files
- Static files are collected to the "staticfiles" directory. In production, WhiteNoise serves them.
- Media files are stored in the "media" directory. In production, serve media via the web server (e.g., Nginx) pointing to MEDIA_ROOT.

Collect static files before deploying:
```
python manage.py collectstatic --noinput
```

## Production run (example with Gunicorn)
```
export DJANGO_DEBUG=False
export DJANGO_ALLOWED_HOSTS="your.domain"
export DJANGO_SECRET_KEY="change-me"
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
# Run the app (adjust workers and bind to your environment)
gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 3
```

Behind Nginx, proxy pass to Gunicorn and let Nginx serve /media/ from the media directory. WhiteNoise will serve /static/ from "staticfiles".
