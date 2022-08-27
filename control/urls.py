from django.urls import path
from . import views

app_name = 'control'

urlpatterns = [
    path('', views.control, name='ctrl'),
    path('ctrl/', views.admin_control, name='admin_ctrl'),
    path('voteaza/', views.voteaza, name="voteaza"),
    path('<int:pk>/', views.votare, name="votare"),
    path('rezultate/', views.rezultate, name="rezultate"),
    path('feedback/', views.feedback, name="feedback"),
]

