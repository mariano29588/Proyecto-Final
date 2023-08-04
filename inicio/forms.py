from django import forms
from .models import Estudiantes

# class CrearEstudianteFormulario(forms.Form):
#     nombre = forms.CharField(max_length=20)
#     apellido = forms.CharField(max_length=20)
#     edad = forms.IntegerField()
#     fecha_nacimiento = forms.DateField(required=False)
#     descripcion = forms.CharField(max_length=4000)
#     imagen = forms.ImageField(required=False)

class CrearEstudianteFormulario(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = ['nombre', 'apellido', 'edad', 'fecha_nacimiento', 'descripcion', 'imagen']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})
        }
 
class BuscarEstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
