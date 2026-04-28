from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Tarea

from .forms import TareaForms
# Create your views here.

def tareas(request):
    tareas = Tarea.objects.filter(activo = True)
    return render(request,"todolist/index.html", {"tareas":tareas})


def crear_tarea(request):
    if request.method =="POST":
        form = TareaForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todolist/index.html')
    else:
        form = TareaForms()
    
    return render(request,'todolist/crar_tarea.html',{'form':form})



# Params ruta: url.com/usuario/5
# Query PArams: url.com/usuarios?clave=valor&clave_sod=valor¬clave_tres=valor


def editar_tarea(request, id):
    
    tarea = get_object_or_404(Tarea, id=id)

    if request.method =='POST':
        form = TareaForms(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect("tarea")
    else:
        form = TareaForms(instance=tarea)
    return render(request, "todolist/editar_tarea.html", {"form":form})



def eliminar_tarea(request, id):
    tarea =get_object_or_404(Tarea, id=id)

    if request.method == "POST":
        tarea.activo = False
        Tarea.save()
        return redirect("tareas")
    return render(request, 'todolist/borrar_tarea.html',{"tarea":tarea})

