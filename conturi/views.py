from django.shortcuts import render, redirect
from . import urls
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import Group
from .forms import UtilizatorForm, inregistrare_form
from django import forms
from .forms import CustomAuthenticationForm
from .models import Profil
from control.forms import FeedbackForm

def autentificareUser(request, user, authenticatedPage):
    try:
        if str(user) == 'coordonator' or str(user) == 'admin':
            login(request, user)
            return redirect('control:admin_ctrl')

        profil = Profil.objects.get(user=user)
        login(request, user)

        if profil.isApproved():
            messages.info(request, 'V-ați autentificat cu succes.')
            return redirect(authenticatedPage)
        else:
            return render(request, 'conturi_templates/user_neacceptat.html')
    except Exception as e:
        print(f'Error {e}')
        return render(request, 'conturi_templates/login.html')

def login_view(request):
    if request.user.is_authenticated:
        return autentificareUser(request, user, 'control:ctrl') ### AICI in loc de request.user la el e doar user

    if request.method == 'POST':
        print("AICI 1")
        form = CustomAuthenticationForm(data=request.POST) ### AICI la el e alt form
        if form.is_valid():
            user = form.get_user()
            print("AICI 2")
            return autentificareUser(request, user, 'control:ctrl')
    else:
        form = CustomAuthenticationForm()
        print("FORM:", form)

    return render(request, 'conturi_templates/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'V-ați deconectat.')
    return redirect('pagina_de_start')

def inregistrare_view(request):

    if request.method == 'POST':
        user_form = UtilizatorForm(request.POST)
        profil_form = inregistrare_form(data=request.POST, files=request.FILES)

        if user_form.is_valid() and profil_form.is_valid():
            user = user_form.save(commit=False)
            user.save()

            profil = profil_form.save(commit=False)
            profil.user = user

            user_group = Group.objects.get(name='Alegator')
            user.groups.add(user_group)

            profil.save()
            print('Only user is saved')

            # log the user in
            login(request, user)
            messages.info(request, 'V-ați înregistrat cu succes!')
            return redirect('conturi:login')
        else:
            print(profil_form.errors.as_data())
            print(user_form.errors.as_data())
            messages.error(request, 'Înregistrare eșuată!')
    else:
        user_form = UtilizatorForm()
        profil_form = inregistrare_form()

    context = {
        'form': user_form,
        'profil': profil_form,
    }
    return render(request, 'conturi_templates/inregistrare.html', context)

def address_creation():
    print("Accessing users ..")
    users = Profil.objects.all()
    print("Assigning addresses to the users")
    # ganache_url = "http://127.0.0.1:8545"
    # web3 = Web3(Web3.HTTPProvider(ganache_url))
    for i in range(100):
        # address = web3.toChecksumAddress(account['address'])
        try:
            obj = Profil.objects.get(id=i)
            # obj.token = accounts[x]
            obj.save()
            print('address assigned to ', users[i])
        except:
            if i >= 100:
                break


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Feedback trimis cu succes.')
            return render(request, 'conturi_templates/user_neacceptat.html')
    else:
        form = FeedbackForm()
    return render(request, 'accounts/feedback.html', {'form': form})