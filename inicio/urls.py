from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('estudiantes/crear/', views.crear_estudiante, name='crear_estudiante'),
]