from django.conf import settings
from django.db import models

class Reminder(models.Model):
    TYPE_CHOICES = [("medication","Medication"),("vaccine","Vaccine")]
    CHANNEL_CHOICES = [("email","Email"),("sms","SMS")]
    RECURRENCE_CHOICES = [
        ("once","One time"),("daily","Daily"),("weekly","Weekly"),("monthly","Monthly")
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reminders")
    name = models.CharField(max_length=200, verbose_name="Medication or vaccine")
    reminder_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="medication")
    dose = models.CharField(max_length=100, blank=True)
    scheduled_at = models.DateTimeField()
    recurrence = models.CharField(max_length=20, choices=RECURRENCE_CHOICES, default="once")
    channel = models.CharField(max_length=10, choices=CHANNEL_CHOICES, default="email")
    phone_number = models.CharField(max_length=30, blank=True)
    active = models.BooleanField(default=True)
    last_sent_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["scheduled_at"]

    def __str__(self):
        return f"{self.name} - {self.scheduled_at:%Y-%m-%d %H:%M}"
