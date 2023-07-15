from django.shortcuts import render
from inicio.forms import CrearEstudianteFormulario, BuscarEstudianteFormulario
from inicio.models import Estudiantes
from django.http import HttpResponse 

from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def info_pagina(request):
    return render(request, 'inicio/info_pagina.html')

@login_required
def crear_estudiante(request):
    mensaje = ''

    if request.method == 'POST':
        formulario = CrearEstudianteFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            estudiante = Estudiantes(nombre=info['nombre'], apellido=info['apellido'], edad=info['edad'], fecha_nacimiento=info['fecha_nacimiento'], descripcion = info['descripcion'])
            estudiante.save()
            mensaje = f'Se creo el estudiante {estudiante.nombre}'
                                    
        else:
            return render(request, 'inicio/crear_estudiante.html', {'formulario': formulario})

    formulario = CrearEstudianteFormulario()
    return render(request, 'inicio/crear_estudiante.html', {'formulario': formulario, 'mensaje': mensaje})


@login_required
def listado_estudiantes(request):

    formulario = BuscarEstudianteFormulario(request.GET)
    listado_estudiantes = []
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data.get('nombre', '')
        listado_estudiantes = Estudiantes.objects.filter(nombre__icontains=nombre_a_buscar)



    formulario = BuscarEstudianteFormulario()
    return render(request, 'inicio/estudiantes.html', {'formulario': formulario, 'listado_estudiantes': listado_estudiantes})
 
                                                       
                                                       

# def listado_estudiantes(request):
#     # formulario = BuscarEstudianteFormulario() 
#     # if request.method == 'GET':
#         formulario = BuscarEstudianteFormulario(request.GET)  

#         if formulario.is_valid():
#             nombre_busqueda = formulario.cleaned_data['nombre']
#             listado_de_estudiantes = Estudiantes.objects.filter(nombre__icontains=nombre_busqueda)
#             return render(request, 'inicio/listado_estudiantes.html', {'formulario': formulario, 'estudiantes': listado_de_estudiantes})
            
            
        # return render(request, 'inicio/listado_estudiantes.html', {'formulario': formulario})




class DetalleEstudiantes(DetailView):
     model = Estudiantes
     template_name = "inicio/detalle_estudiantes.html"


class ModificarEstudiantes(UpdateView):
     model = Estudiantes
     fields = ['nombre', 'apellido', 'edad', 'fecha_nacimiento', 'descripcion']
     template_name = "inicio/modificar_estudiantes.html"
     success_url = reverse_lazy('inicio:estudiantes')
     

class EliminarEstudiantes(DeleteView):
    model = Estudiantes
    template_name = "inicio/eliminar_estudiantes.html"
    success_url = reverse_lazy('inicio:estudiantes')









             # print(nombre_busqueda) 
        # else:
        #     print('no es valido')

          

        

#         formulario = BuscarEstudianteFormulario()

#         if request.method =='GET':
#             formulario = BuscarEstudianteFormulario(request.GET)
#             if formulario.is_valid()
#             nombre_busqueda = formulario.cleaned_data['nombre']

#         return render(request, 'inicio/listado_estudiantes.html', {'formulario': formulario})