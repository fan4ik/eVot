from django import forms
from control.models import Candidat
from django.contrib.auth.models import User

class AdaugaCandidat(forms.ModelForm):
    class Meta:
        model = Candidat
        fields = ("nume", "echipa")
        widgets = {
            'nume': forms.TextInput(attrs={'class': 'form-control'}),
            'echipa': forms.TextInput(attrs={'class': 'form-control'})
        }

class AddUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username","first_name","last_name","email")
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'})
           }