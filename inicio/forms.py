from django import forms

class CrearEstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField(required=False)
    descripcion = forms.CharField(max_length=4000)
 
class BuscarEstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
