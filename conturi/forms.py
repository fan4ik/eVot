from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from .models import Profil

from django.contrib.auth.forms import AuthenticationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

# Am redenumit username si password
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
        self.fields['username'].label = 'Identificator'
        self.fields['password'].label = 'Parola'

class UtilizatorForm(UserCreationForm):
    first_name = forms.CharField(label='Prenume', max_length=50)
    first_name.widget.attrs.update({'class': 'form-control'})

    last_name = forms.CharField(label='Nume', max_length=50)
    last_name.widget.attrs.update({'class': 'form-control'})

    email = forms.EmailField()
    email.widget.attrs.update({'class': 'form-control'})

    password1 = forms.CharField(label='Parola',
                                strip=False,
                                widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())

    password2 = forms.CharField(label='Confirmați Parola',
                                strip=False,
                                widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}
        help_texts = {"username": 'username'}


    def clean(self):
        super(UtilizatorForm, self).clean()

      # getting username and password from cleaned_data
        username = self.cleaned_data.get('username')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

      # validating the username and password
        print(username)
        print(type(username))
        print(len(str(username)))

        if len(username) < 5:
            print('Username-ul trebuie să conțină 5-14 caractere.')
            self._errors['username'] = self.error_class(['Username-ul trebuie să conțină 5-14 caractere.'])
        if len(username) > 14:
            self._errors['username'] = self.error_class(['Username-ul trebuie să conțină 5-14 caractere.'])
        if len(last_name) < 3:
            self._errors['last_name'] = self.error_class(['Nume: Minim - 3 caractere.'])
        if len(last_name) > 50:
            self._errors['last_name'] = self.error_class(['Nume: Maxim - 50 caractere.'])
        if len(first_name) < 3:
            self._errors['first_name'] = self.error_class(['Prenume: Minim - 3 caractere.'])
        if len(first_name) > 50:
            self._errors['first_name'] = self.error_class(['Prenume: Maxim - 50 caractere.'])

        return self.cleaned_data

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['password1'].help_text = ''
            self.fields['password2'].help_text = ''


class inregistrare_form(forms.ModelForm):

    GEN = (('1', 'M'),
           ('2', 'F'))

    gen = forms.ChoiceField(choices=GEN)
    gen.widget.attrs.update({'class': 'form-control'})

    data_nastere = forms.DateField()
    data_nastere.widget.attrs.update({'placeholder': 'AAAA-LL-ZZ'})
    data_nastere.widget.attrs.update({'class': 'form-control'})
    data_nastere.widget.attrs.update({'onfocus': 'this.type="date"'})
    data_nastere.widget.attrs.update({'onblur': 'this.type="text"'})

    localitate = forms.CharField(max_length=100)
    localitate.widget.attrs.update({'class': 'form-control'})

    adresa = forms.CharField(max_length=100)
    adresa.widget.attrs.update({'class': 'form-control'})

    nr_telefon = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='RO'))
    nr_telefon.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Profil
        fields = ['gen', 'data_nastere', 'localitate', 'adresa', 'nr_telefon', 'document_fata', 'document_verso']