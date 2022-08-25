from django.shortcuts import render

def pagina_de_start(request):
    return render(request, 'eVot_templates/pagina_de_start.html')

def info(request):
    return render(request, 'eVot_templates/info.html')