from datetime import timedelta
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
from reminders.models import Reminder

def next_time(dt, recurrence):
    if recurrence == "daily": return dt + timedelta(days=1)
    if recurrence == "weekly": return dt + timedelta(days=7)
    if recurrence == "monthly": return dt + timedelta(days=30)
    return None

def send_sms(to, body):
    if not (settings.TWILIO_ACCOUNT_SID and settings.TWILIO_AUTH_TOKEN and settings.TWILIO_PHONE_NUMBER):
        raise RuntimeError("Twilio is not configured.")
    from twilio.rest import Client
    Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN).messages.create(
        body=body, from_=settings.TWILIO_PHONE_NUMBER, to=to
    )

def handle():
    now = timezone.now()
    due = Reminder.objects.select_related("user").filter(active=True, scheduled_at__lte=now)
    sent = 0
    for r in due:
        body = f"HealthBot reminder: {r.name}"
        if r.dose:
            body += f" — dose: {r.dose}"
        if r.reminder_type == "vaccine":
            body += ". Please follow your clinician's vaccination schedule."
        try:
            if r.channel == "email":
                send_mail("HealthBot reminder", body, settings.DEFAULT_FROM_EMAIL, [r.user.email], fail_silently=False)
            else:
                send_sms(r.phone_number, body)
            r.last_sent_at = now
            nxt = next_time(r.scheduled_at, r.recurrence)
            if nxt:
                while nxt <= now:
                    nxt = next_time(nxt, r.recurrence)
                r.scheduled_at = nxt
            else:
                r.active = False
            r.save(update_fields=["last_sent_at","scheduled_at","active"])
            sent += 1
        except Exception as exc:
            print(f"Reminder {r.pk} failed: {exc}")
    print(f"Processed {sent} reminder(s).")

from django.core.management.base import BaseCommand
class Command(BaseCommand):
    help = "Send all due medication/vaccine reminders."
    def handle(self, *args, **kwargs):
        handle()
