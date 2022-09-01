from django.shortcuts import render, redirect, get_object_or_404
from conturi.models import Profil
from conturi.views import address_creation
from control.models import Candidat, Feedback
from django.contrib.auth.models import User
from .forms import adaugaCandidat, adaugaUser
from .decorators import allowed_users
from .models import Alegere
from control.functions import adauga_Candidat

#@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def coordonator(request):
    alegere = Alegere.objects.get(id=1)
    nr_candidati = Candidat.objects.all().count()
    nr_utilizatori = Profil.objects.all().count()
    nr_cereri_feedback = Feedback.objects.all().count()
    return render(request, 'coordonator_templates/coordonator.html', {
        'cancount': nr_candidati,
        'usercount': nr_utilizatori,
        'quarycount': nr_cereri_feedback,
        'status_Alegere': alegere.status_Alegere
    })


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def candidati(request):
    candidati_date = Candidat.objects.all()
    return render(request, 'coordonator_templates/candidat.html', {'candidati_date': candidati_date})


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def adauga_candidat(request):
    fm = adaugaCandidat(request.POST)
    if fm.is_valid():
        fm.save()
        return redirect('/coordonator/candidati')
    else:
        return render(request, 'coordonator_templates/adauga_candidat.html', {'form': fm})


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def sterge_candidat(request):
    data = request.POST
    id = data.get('id')
    canddata = Candidat.objects.get(id=id)
    canddata.delete()
    return redirect('/coordonator/candidati')


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def edit_candidat(request, id):
    context = {}
    obj = get_object_or_404(Candidat, id=id)
    form = adaugaCandidat(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('/coordonator/candidati')

    context["form"] = form
    return render(request, "coordonator_templates/edit_candidat.html", context)


# USER CRUD OPERATIONS
@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def afiseaza_user(request):
    utilizatori = User.objects.all()
    print("++++++++++++++++++++++++++ ", utilizatori)
    for i in range(len(utilizatori)):
        print(utilizatori[i].username)
    return render(request, 'coordonator_templates/user.html', {'utilizatori': utilizatori})

'''
@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def adauga_user(request):
    fm = adaugaUser(request.POST)
    if fm.is_valid():
        fm.save()
        return redirect('/coordonator/utilizatori')
    else:
        return render(request, 'coordonator_templates/adauga_user.html', {'form': fm})
'''

@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def sterge_user(request):
    data = request.POST
    id = data.get('id')
    userdata = User.objects.get(id=id)
    userdata.delete()
    return redirect('/coordonator/utilizatori')


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def edit_user(request, id):
    context = {}
    obj = get_object_or_404(User, id=id)
    form = adaugaUser(request.POST or None, instance=obj)
    print("FORM: ", form)
    if form.is_valid():
        form.save()
        return redirect('/coordonator/utilizatori')

    context["form"] = form
    return render(request, "coordonator_templates/edit_user.html", context)


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def feedback(request):
    feedback_date = Feedback.objects.all()
    return render(request, 'coordonator_templates/cereri_feedback.html', {
        'feedback_date': feedback_date
    })


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def cerere_rezolvata(request):
    data = request.POST
    id = data.get('id')
    quariesdata = Feedback.objects.get(id=id)
    quariesdata.delete()
    return redirect('/coordonator/feedback')


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def aproba_candidati(request):
    print("Approving candidate...")
    candidat = Candidat.objects.all()
    adauga_Candidat(candidat)
    print("Candidate Approved...")


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def start_alegere(request):
    address_creation()
    aproba_candidati(request)
    print("START ALEGERI.")
    return redirect('/coordonator/')


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def stop_alegere(request):
    alegere = Alegere.objects.get(id=1)
    alegere.status_Alegere = False
    alegere.isCandidateAdded = False
    alegere.save()
    print("STOP ALEGERI.")
    return redirect('/coordonator/')

@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def aprobare(request):
    try:
        lista_aprobare = []
        users = list(Profil.objects.all())
        print("USERS: ", users)
        primaryKeys = [u.pk for u in users]
        print("PK: ", primaryKeys)
        for i in range(len(primaryKeys)):
            print("i: ", i)
            user = Profil.objects.get(id=primaryKeys[i])
            if user.isApproved():
                pass
            else:
                lista_aprobare.append(user)
        if lista_aprobare:
            return render(request, 'coordonator_templates/aproba.html', {'listaUtilizatori_aprobare': lista_aprobare})
        else:
            return render(request, 'coordonator_templates/listaAprobare_null.html')
    except Exception as e:
        print(f'Eroare la coordonator:aproba\n {e}')


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def sterge_profil(request):
    data = request.POST
    id = data.get('id')
    userdata = User.objects.get(id=id)
    userdata.delete()
    return redirect('/coordonator/aproba/')

@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def aproba_profil(request, id):
    user = Profil.objects.get(id=id)
    user.getApproved()
    user.save()
    return redirect('/coordonator/aproba/')