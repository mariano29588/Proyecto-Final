from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # path('estudiantes/crear/', views.crear_estudiante, name='crear_estudiante'),
    path('estudiantes/crear/', views.crear_estudiante, name='crear_estudiante'),
    path('estudiantes/', views.listado_estudiantes, name='estudiantes'),
    path('estudiantes/<int:pk>/', views.DetalleEstudiantes.as_view(), name='detalle_estudiantes'),
    path('estudiantes/<int:pk>/modificar/', views.ModificarEstudiantes.as_view(), name='modificar_estudiantes'),
    path('estudiantes/<int:pk>/eliminar/', views.EliminarEstudiantes.as_view(), name='eliminar_estudiantes'),
]

