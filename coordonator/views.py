from django.shortcuts import render, redirect, get_object_or_404
from conturi.models import Profil
from conturi.views import address_creation
from control.models import Candidat, Feedback
from django.contrib.auth.models import User
from .forms import AdaugaCandidat, AddUser
from .decorators import allowed_users
from coordonator.forms import AdaugaCandidat
from .models import Alegere


# Create your views here.
#@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def coordonator(request):
    print("coordonator.views.coordonator()")
    is_status = Alegere.objects.get(id=1)
    can_count = Candidat.objects.all().count()
    user_count = Profil.objects.all().count()
    quary_count = Feedback.objects.all().count()
    return render(request, 'coordonator_templates/coordonator.html', {
        'cancount': can_count,
        'usercount': user_count,
        'quarycount': quary_count,
        'status': is_status.status
    })


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def candidate(request):
    can_data = Candidat.objects.all()
    return render(request, 'officer/candidate.html', {
        'candata': can_data
    })


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def add_candidate(request):
    fm = AdaugaCandidat(request.POST)
    if fm.is_valid():
        fm.save()
        return redirect('/officer/candidates')
    else:
        return render(request, 'officer/add-candidate.html', {'form': fm})


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def delete_candidate(request):
    data = request.POST
    id = data.get('id')
    canddata = Candidat.objects.get(id=id)
    canddata.delete()
    return redirect('/officer/candidates')


# def edit_candidate(request, id):
#     cand = Candidate.objects.get(id=id)
#     fm = AddCandidate(request.POST)
#     return render(request, 'edit-candidate.html', {'form':fm})
#     if fm.is_valid():
#         fm.save()
#         return redirect('/officer')

@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def edit_candidate(request, id):
    context = {}
    obj = get_object_or_404(Candidat, id=id)
    form = AdaugaCandidat(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('/officer/candidates')

    context["form"] = form
    return render(request, "officer/edit-candidate.html", context)


# USER CRUD OPERATIONS
@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def realuser(request):
    user_data = User.objects.all()
    return render(request, 'officer/user.html', {
        'userdata': user_data
    })


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def add_user(request):
    fm = AddUser(request.POST)
    if fm.is_valid():
        fm.save()
        return redirect('/officer/users')
    else:
        return render(request, 'officer/add-user.html', {'form': fm})


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def delete_user(request):
    data = request.POST
    id = data.get('id')
    userdata = User.objects.get(id=id)
    userdata.delete()
    return redirect('/officer/users')


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def edit_user(request, id):
    context = {}
    obj = get_object_or_404(User, id=id)
    form = AddUser(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('/officer/users')

    context["form"] = form

    return render(request, "officer/edit-user.html", context)


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def quaries(request):
    quaries_data = Feedback.objects.all()
    return render(request, 'officer/contact_res.html', {
        'quariesdata': quaries_data
    })


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def quarysolved(request):
    data = request.POST
    id = data.get('id')
    quariesdata = Feedback.objects.get(id=id)
    quariesdata.delete()
    return redirect('/officer/quaries')


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def Approved_candidate(request):
    print("Approving candidate...")
    candidate = Candidat.objects.all()
    add_Candidate(candidate)
    print("Candidate Approved...")


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def start_election(request):
    address_creation()
    Approved_candidate(request)
    return redirect('/officer/')


@allowed_users(allowed_roles=['Admin', 'Coordonator'])
def end_election(request):
    is_sts = Alegere.objects.get(id=1)
    is_sts.status = False
    is_sts.isCandidateAdded = False
    is_sts.save()
    return redirect('/officer/')

@allowed_users(allowed_roles=['Admin', 'Staff'])
def user_approval(request):
    users = list(Profil.objects.all())
    primaryKeys = [x.pk for x in users ]
    for i in range(len(primaryKeys)) :
        user_inst = Profil.objects.get(id=primaryKeys[i])
        if user_inst.isApproved():
            users.pop(i)
    print(users)
    return render(request,'officer/approve.html',{
        'userdata':users
    })


@allowed_users(allowed_roles=['Admin', 'Staff'])
def del_profile(request):
    data = request.POST
    id = data.get('id')
    userdata = User.objects.get(id=id)
    userdata.delete()
    return redirect('/officer/approve/')

@allowed_users(allowed_roles=['Admin', 'Staff'])
def approve_profile(request, id):
    user_inst = Profil.objects.get(id=id)
    user_inst.getApproved()
    user_inst.save()
    return redirect('/officer/approve/')