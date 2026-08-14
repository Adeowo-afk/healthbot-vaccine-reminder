from django.contrib import admin
from .models import Reminder
@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ("name","user","reminder_type","scheduled_at","channel","active","last_sent_at")
    list_filter = ("reminder_type","channel","active","recurrence")
    search_fields = ("name","user__username","user__email")
