from django.urls import path
from .views import SiteLoginView, SiteLogoutView

urlpatterns = [
    path('login/', SiteLoginView.as_view(), name='auth.login'),
    path('logout/', SiteLogoutView.as_view(), name='auth.logout'),
]
