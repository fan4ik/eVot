from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'conturi'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('inregistrare/', views.inregistrare_view, name='inregistrare'),
    path('feedback/', views.feedback_view, name='feedback')
]