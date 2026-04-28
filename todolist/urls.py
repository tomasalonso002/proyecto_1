from django.urls import path, include
from . import views

urlpatterns = [
        path('tareas/', views.tareas, name="tarea"),
        path('nueva/', views.crear_tarea, name="crar_tarea"),
        path('editar/<int:id>', views.editar_tarea, name="editar"),
        path('borrar/<int:id>', views.eliminar_tarea, name="borrar")
]