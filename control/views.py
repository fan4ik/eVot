from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm
from django.contrib import messages
from .models import Candidat
from coordonator.models import Alegere
from coordonator.views import coordonator
from conturi.models import Profil
from . import functions

lista_votanti = []

@login_required(login_url="/conturi/login")
def control(request):
    try:
        user = request.user
        if str(user) == 'coordonator' or str(user) == 'admin':
            return redirect('control:adminctrl')
        profile = Profil.objects.get(user=user)
        if profile.isApproved():
            return render(request, 'control_templates/pagina_informativa.html')
        else:
            return render(request, 'conturi_templates/user_neacceptat.html')
    except Exception as e:
        print(f'Eroare: {e}')
        return render(request, 'conturi_templates/user_neacceptat.html')


@login_required(login_url="/conturi/login")
def voteaza(request):
    alegere = Alegere.objects.get(id=1)

    if alegere.status == True:
        candidati = Candidat.objects.all()
        return render(request, 'control_templates/voteaza.html', {'candidati': candidati})
    else:
        return render(request, 'control_templates/NuAmVotat.html')

# @login_required(login_url="/accounts/submitvote")
def votare(request, pk):
    nume_candidat_votat = Candidat.objects.get(id=pk)
    alegator_token = Profil.objects.get(user=request.user)
    token = alegator_token.token
    try:
        if (token in lista_votanti):
            return render(request, 'control_templates/AmVotatDeja.html')
        else:
            lista_votanti.append(token)
            hashr = functions.Transactions(nume_candidat_votat, alegator_token.token)
            print(hashr)
            return render(request, 'control_templates/AmVotat_Succes.html')
    except:
        return render(request, 'control_templates/AmVotatDeja.html')


def rezultate(request):
    alegere = Alegere.objects.get(id=1)
    if (alegere.status):
        return render(request, 'control_templates/rezultate_null.html')
    else:
        try:
            rezultate = functions.rezultate_finale()
        except:
            print('Eroare la control:rezultate')
            return render(request, 'control_templates/rezultate_null.html')
        return render(request, 'control_templates/rezultate.html', {
            'candidat': rezultate['candidati'],
            'rezultate': rezultate['nr_voturi']
        })


@login_required(login_url="/conturi/login")
def admin_control(request):
    return coordonator(request)

def feedback(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return render(request, 'dashboard.html')
    else:
        f = FeedbackForm()
    return render(request, 'contact.html', {'form': f})