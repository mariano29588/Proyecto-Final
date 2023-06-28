from django.shortcuts import render
from inicio.forms import CrearEstudianteFormulario, BuscarEstudianteFormulario
from inicio.models import Estudiantes
from django.http import HttpResponse 

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

# def listado_estudiantes(request):
        
#       return render(request, 'inicio/listado_estudiantes.html', {'formulario': formulario})



def listado_estudiantes(request):
    # formulario = BuscarEstudianteFormulario() 
    # if request.method == 'GET':
        formulario = BuscarEstudianteFormulario(request.GET)  

        if formulario.is_valid():
            nombre_busqueda = formulario.cleaned_data['nombre']
            listado_de_estudiantes = Estudiantes.objects.filter(nombre__icontains=nombre_busqueda)
            return render(request, 'inicio/listado_estudiantes.html', {'formulario': formulario, 'estudiantes': listado_de_estudiantes})
            
            
        return render(request, 'inicio/listado_estudiantes.html', {'formulario': formulario})
            # print(nombre_busqueda) 
        # else:
        #     print('no es valido')

          

        

#         formulario = BuscarEstudianteFormulario()

#         if request.method =='GET':
#             formulario = BuscarEstudianteFormulario(request.GET)
#             if formulario.is_valid()
#             nombre_busqueda = formulario.cleaned_data['nombre']

#         return render(request, 'inicio/listado_estudiantes.html', {'formulario': formulario})

