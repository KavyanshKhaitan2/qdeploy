from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Project

# Create your views here.


class HomepageView(LoginRequiredMixin, View):
    def get(self, request):
        projects = Project.objects.all()
        return render(request, "dashboard/index.html", context={"projects": projects})


class CreateProjectView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "projects/create.html")

    def post(self, request):
        name: str = request.POST["name"]
        description: str = request.POST.get("description", "")
        repo_url: str = request.POST.get("repo")
        project = Project(name=name, description=description, repo_url=repo_url, deployed=False)
        project.save()
        messages.success(request, f"Created project with id {project.pk}.")
        return redirect(self.request.path_info)
