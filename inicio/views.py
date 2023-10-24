from django.shortcuts import render
from inicio.models import Paleta

def inicio(request):
    
    return render(request, 'inicio/inicio.html', {})

def paletas(request):
    
    paleta = Paleta(nombre='christian', apellido='burns', edad='38', descripcion='programador')
    paleta.save()
    
    return render(request, 'inicio/paletas.html', {'paleta': paleta})
