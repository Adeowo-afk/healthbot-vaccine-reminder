from django.urls import path
from . import views
urlpatterns = [
    path("new/", views.create_reminder, name="reminder_create"),
    path("<int:pk>/edit/", views.edit_reminder, name="reminder_edit"),
    path("<int:pk>/delete/", views.delete_reminder, name="reminder_delete"),
]
