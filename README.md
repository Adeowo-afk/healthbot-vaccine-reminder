# HealthBot — Vaccine & Medication Reminder Bot

A production-oriented Django starter app for medication and vaccination reminders.

## Features
- Customer signup/login
- Customer dashboard
- Medication/vaccine CRUD
- One-time, daily, weekly, monthly schedules
- Email reminders
- Optional Twilio SMS
- Django admin/superuser
- PostgreSQL-ready production configuration
- Render Blueprint with public web service + Postgres + per-minute cron

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000

For local testing of reminders:
```bash
python manage.py send_due_reminders
```

## Environment variables

For email, set:
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=...
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=...
EMAIL_HOST_PASSWORD=...
DEFAULT_FROM_EMAIL=...

For SMS, set:
TWILIO_ACCOUNT_SID=...
TWILIO_AUTH_TOKEN=...
TWILIO_PHONE_NUMBER=...

For automatic production admin creation:
ADMIN_USERNAME=...
ADMIN_EMAIL=...
ADMIN_PASSWORD=...

## Public deployment

Recommended easiest path: Render.
1. Push this folder to GitHub.
2. In Render, create a new Blueprint and select the repository.
3. Render will create the web app and Postgres database from render.yaml.
4. Add the email/Twilio and admin environment variables.
5. The cron service runs every minute and calls send_due_reminders.

IMPORTANT: The reminder bot is a scheduling/notification tool, not medical advice. Users should follow their clinician's instructions and official vaccination schedules.
