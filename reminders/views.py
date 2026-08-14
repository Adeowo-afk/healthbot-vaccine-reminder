from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ReminderForm
from .models import Reminder

def home(request):
    if request.user.is_authenticated:
        return render(request, "reminders/dashboard.html", {"reminders": request.user.reminders.all()})
    return render(request, "reminders/home.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

@login_required
def create_reminder(request):
    form = ReminderForm(request.POST or None)
    if form.is_valid():
        r = form.save(commit=False)
        r.user = request.user
        if r.channel == "sms" and not r.phone_number:
            form.add_error("phone_number", "Phone number is required for SMS.")
        else:
            r.save()
            messages.success(request, "Reminder saved.")
            return redirect("home")
    return render(request, "reminders/form.html", {"form": form, "title": "Add reminder"})

@login_required
def edit_reminder(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk, user=request.user)
    form = ReminderForm(request.POST or None, instance=reminder)
    if form.is_valid():
        form.save()
        messages.success(request, "Reminder updated.")
        return redirect("home")
    return render(request, "reminders/form.html", {"form": form, "title": "Edit reminder"})

@login_required
def delete_reminder(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk, user=request.user)
    if request.method == "POST":
        reminder.delete()
        messages.success(request, "Reminder deleted.")
        return redirect("home")
    return render(request, "reminders/confirm_delete.html", {"reminder": reminder})
