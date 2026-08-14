from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from reminders.views import home, signup

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("signup/", signup, name="signup"),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("reminders/", include("reminders.urls")),
]
