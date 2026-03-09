from django.urls import path
from .views import HomepageView, SiteLoginView, SiteLogoutView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('login/', SiteLoginView.as_view(), name='auth.login'),
    path('logout/', SiteLogoutView.as_view(), name='auth.logout'),
]
