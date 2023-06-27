from django.shortcuts import render
from inicio.forms import CrearEstudianteFormulario
from inicio.models import Estudiantes

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def crear_estudiante(request):
    mensaje = ''

    if request.method == 'POST':
        formulario = CrearEstudianteFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            estudiante = Estudiantes(nombre=info['nombre'],edad=info['edad'], fecha_nacimiento=info['fecha_nacimiento'])
            estudiante.save()
            mensaje = f'Se creo el estudiante {estudiante.nombre}'
            
        else:
            return render(request, 'inicio/crear_estudiante.html', {'formulario': formulario})

    formulario = CrearEstudianteFormulario()
    return render(request, 'inicio/crear_estudiante.html', {'formulario': formulario, 'mensaje': mensaje})