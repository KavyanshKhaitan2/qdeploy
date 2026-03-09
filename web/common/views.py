from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class HomepageView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'homepage/index.html')

class SiteLoginView(LoginView):
    template_name = "auth/login.html"

class SiteLogoutView(LogoutView):
    template_name = "auth/logout.html"
