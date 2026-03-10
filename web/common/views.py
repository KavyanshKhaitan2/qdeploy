from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class SiteLoginView(LoginView):
    template_name = "auth/login.html"

class SiteLogoutView(LogoutView):
    template_name = "auth/logout.html"
