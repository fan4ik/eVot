from django.urls import path
from . import views

app_name = 'coordonator'

urlpatterns = [
    path('', views.coordonator, name="officercrud"),
    path('candidates', views.candidate, name="cand"),
    path('users', views.realuser, name="user"),
    path('quaries', views.quaries, name="quary"),
    path('quariessolved/', views.quarysolved, name="quarysolved"),
    path('addcand/', views.add_candidate, name="addcand"),
    path('delcand/', views.delete_candidate, name="delcand"),
    path('editcand/<int:id>/', views.edit_candidate, name="editcand"),
    path('deluser/', views.delete_user, name="deluser"),
    path('edituser/<int:id>/', views.edit_user, name="edituser"),
    path('electionstarted/', views.start_election, name="startelection"),
    path('electionended/', views.end_election, name="endelection"),
]