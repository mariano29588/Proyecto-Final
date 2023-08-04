from django.db import models
from ckeditor.fields import RichTextField

class Estudiantes(models.Model):
        nombre = models.CharField(max_length=20)
        apellido = models.CharField(max_length=20, null=True)
        edad = models.IntegerField()
        fecha_nacimiento = models.DateField(null=True)
        descripcion = RichTextField(null=True)
        imagen = models.ImageField(upload_to='estudiantes_images/', null=True, blank=True) 

        def __str__(self):
                return f'Nombre: {self.nombre} - Edad:  {self.edad}'
