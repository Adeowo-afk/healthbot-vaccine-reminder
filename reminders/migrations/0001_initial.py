from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(
            name="Reminder",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200, verbose_name="Medication or vaccine")),
                ("reminder_type", models.CharField(choices=[("medication","Medication"),("vaccine","Vaccine")], default="medication", max_length=20)),
                ("dose", models.CharField(blank=True, max_length=100)),
                ("scheduled_at", models.DateTimeField()),
                ("recurrence", models.CharField(choices=[("once","One time"),("daily","Daily"),("weekly","Weekly"),("monthly","Monthly")], default="once", max_length=20)),
                ("channel", models.CharField(choices=[("email","Email"),("sms","SMS")], default="email", max_length=10)),
                ("phone_number", models.CharField(blank=True, max_length=30)),
                ("active", models.BooleanField(default=True)),
                ("last_sent_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="reminders", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering":["scheduled_at"]},
        ),
    ]
