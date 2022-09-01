from django import forms
from control.models import Candidat
from django.contrib.auth.models import User

class adaugaCandidat(forms.ModelForm):
    class Meta:
        model = Candidat
        fields = ("nume", "echipa")
        widgets = {
            'nume': forms.TextInput(attrs={'class': 'form-control'}),
            'echipa': forms.TextInput(attrs={'class': 'form-control'})
        }

class adaugaUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'username': 'Username',
            'first_name': 'Prenume',
            'last_name': 'Nume',
            'email': 'Email'
        }