from django.urls import path
from .views import HomepageView, CreateProjectView

urlpatterns = [
    path('', HomepageView.as_view(), name='dashboard'),
    path('projects/new/', CreateProjectView.as_view(), name='projects.create')
]
