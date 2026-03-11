from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project

# Create your views here.


class HomepageView(LoginRequiredMixin, View):
    def get(self, request):
        projects = Project.objects.all()
        return render(request, "dashboard/index.html", context={"projects": projects})
