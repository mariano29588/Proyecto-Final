from django.urls import path
from inicio import views 
from django.conf.urls.static import static
from django.conf import settings

app_name = 'inicio'

urlpatterns = [
    path('info_pagina/', views.info_pagina, name='info_pagina'),
    path('', views.inicio, name='inicio'),
    path('estudiantes/crear/', views.crear_estudiante, name='crear_estudiante'),
    path('estudiantes/', views.listado_estudiantes, name='estudiantes'),
    path('estudiantes/<int:pk>/', views.DetalleEstudiantes.as_view(), name='detalle_estudiantes'),
    path('estudiantes/<int:pk>/modificar/', views.ModificarEstudiantes.as_view(), name='modificar_estudiantes'),
    path('estudiantes/<int:pk>/eliminar/', views.EliminarEstudiantes.as_view(), name='eliminar_estudiantes'),
    # path('ckeditor/', include('ckeditor_uploader.urls')),   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)