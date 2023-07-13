from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('estudiantes/crear/', views.crear_estudiante, name='crear_estudiante'),
    path('estudiantes/', views.listado_estudiantes, name='listado_estudiantes'),
    path('estudiantes/int:pk>/', views.detalle_estudiantes, name='detalle_estudiantes')
    
]

