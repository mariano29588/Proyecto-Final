from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from inicio.forms import CrearEstudianteFormulario, BuscarEstudianteFormulario
from inicio.models import Estudiantes
from django.http import HttpResponse 

from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



def inicio(request):
    return render(request, 'inicio/inicio.html')

def info_pagina(request):
    return render(request, 'inicio/info_pagina.html')

@login_required
def crear_estudiante(request):
    mensaje = ''

    if request.method == 'POST':
        formulario = CrearEstudianteFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            estudiante = Estudiantes(nombre=info['nombre'], apellido=info['apellido'], edad=info['edad'], fecha_nacimiento=info['fecha_nacimiento'], descripcion = info['descripcion'], imagen=info['imagen'])
            estudiante.save()
            mensaje = f'Se creo el estudiante {estudiante.nombre}'
                                    
        else:
            return render(request, 'inicio/crear_estudiante.html', {'formulario': formulario})

    formulario = CrearEstudianteFormulario()
    return render(request, 'inicio/crear_estudiante.html', {'formulario': formulario, 'mensaje': mensaje})


@login_required
def listado_estudiantes(request):

    formulario = BuscarEstudianteFormulario(request.GET)
    listado_estudiantes = Estudiantes.objects.all()
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data.get('nombre', '')
        listado_estudiantes = Estudiantes.objects.filter(nombre__icontains=nombre_a_buscar)

    

    formulario = BuscarEstudianteFormulario()
    return render(request, 'inicio/estudiantes.html', {'formulario': formulario, 'listado_estudiantes': listado_estudiantes})
 
class DetalleEstudiantes(DetailView):
     model = Estudiantes
     template_name = "inicio/detalle_estudiantes.html"


@login_required
def modificar_estudiantes(request, estudiante_id):
    estudiante = get_object_or_404(Estudiantes, pk=estudiante_id)

    if request.method == 'POST':
        form = CrearEstudianteFormulario(request.POST, request.FILES, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('inicio:estudiantes')

    else:
        form = CrearEstudianteFormulario(instance=estudiante)

    return render(request, 'inicio/modificar_estudiantes.html', {'form': form, 'estudiantes': estudiante})


# class ModificarEstudiantes(UpdateView):
#      model = Estudiantes
#      fields = ['nombre', 'apellido', 'edad', 'fecha_nacimiento', 'descripcion']
#      template_name = "inicio/modificar_estudiantes.html"
#      success_url = reverse_lazy('inicio:estudiantes')

class ModificarEstudiantes(UpdateView):
    model = Estudiantes
    form_class = CrearEstudianteFormulario
    template_name = "inicio/modificar_estudiantes.html"
    success_url = reverse_lazy('inicio:estudiantes')
     

class EliminarEstudiantes(DeleteView):
    model = Estudiantes
    template_name = "inicio/eliminar_estudiantes.html"
    success_url = reverse_lazy('inicio:estudiantes')

