from django import forms
from .models import Reminder

class ReminderForm(forms.ModelForm):
    scheduled_at = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type":"datetime-local"}),
        input_formats=["%Y-%m-%dT%H:%M"]
    )
    class Meta:
        model = Reminder
        fields = ["name","reminder_type","dose","scheduled_at","recurrence","channel","phone_number","active"]
        widgets = {"active": forms.CheckboxInput(attrs={"class":"form-check-input"})}
