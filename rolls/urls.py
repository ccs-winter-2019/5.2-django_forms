"""
Rolls app urls
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views

app_name = 'rolls'

urlpatterns = [
    # Paths for our django form demo
    path('', views.HomeView.as_view(), name='index'),
    path('create/', views.RollCreateView.as_view(), name='create'),

    # Paths from previous demo
    path('detail/<int:awesome>/', views.DetailView.as_view(), name='detail'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
]
