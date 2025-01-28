# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import CrearTarea

# Create your views here.
def index(request):
    tareas = CrearTarea.objects.all()
    
    # Pasar las tareas al contexto
    context = {
        'tareas': tareas,  # Pasamos todas las tareas a la plantilla
    }
    
    return render(request, "resources/index.html", context)
  
def crearTarea(request):
    if request.method == "POST":
      titulo = request.POST.get("titulo")
      descripcion = request.POST.get("descripcion")
      fecha = request.POST.get("fecha")
      
      nueva_tarea = CrearTarea(titulo_tarea=titulo, descrip_tarea=descripcion, fechaLim_tarea=fecha)
      nueva_tarea.save()
      
      # Redirigir a la página de lista de tareas después de crear la tarea
      return redirect("index")
    return render(request, "resources/crearTarea.html")