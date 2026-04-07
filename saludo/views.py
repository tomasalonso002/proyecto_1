
from django.http import HttpResponse
from django.shortcuts import render

contexto = {
    "nombre":"juancito",
    "esMayor":True,
    "mascotas":["Firulais", "Bobby", "Michigan"]
    }

def saludo(request):
    return render(request, 'saludo/index.html', contexto)

def despedir(request):
    return render(request, 'saludo/despedir.html', contexto)

def inicio(request):
    return HttpResponse("<h1>Estoy en root. (localhost:8000)</h1>")