from django.urls import path
from . import views

app_name = 'coordonator'

urlpatterns = [
    path('', views.coordonator, name="officercrud"),
    path('candidati', views.candidati, name="candidati"),
    path('utilizatori', views.afiseaza_user, name="user"),
    path('feedback', views.feedback, name="feedback"),
    path('quariessolved/', views.cerere_rezolvata, name="cerere_rezolvata"),
    path('addcand/', views.adauga_candidat, name="addcand"),
    path('delcand/', views.sterge_candidat, name="delcand"),
    path('editcand/<int:id>/', views.edit_candidat, name="edit_candidat"),
    #path('adauga_user/', views.adauga_user, name="adauga_user"),
    path('deluser/', views.sterge_user, name="sterge_user"),
    path('edituser/<int:id>/', views.edit_user, name="edit_user"),
    path('electionstarted/', views.start_alegere, name="startelection"),
    path('electionended/', views.stop_alegere, name="endelection"),
    path('aproba/', views.aprobare, name="aproba"),
    path('delprofile/', views.sterge_profil, name="delprofile"),
    path('appProfile/<int:id>/', views.aproba_profil, name="approveprofile"),
]