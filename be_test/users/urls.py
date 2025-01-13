from django.urls import path
from . import views
from .views import validate_password

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/member_details/<int:id>', views.member_details, name='member_details'),
    path('', views.main, name='main'),
    path('testing/', views.testing, name='testing'),
    path('home/', views.Home.as_view(), name='home'),
    path('api/validate_password/', validate_password, name='validate_password'),
]