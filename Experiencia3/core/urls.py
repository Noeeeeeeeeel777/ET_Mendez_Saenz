from django.urls import path
from .views import inicio, quienes_somos, Galeria_imagenes, Api, nuevo_formulario_, mostrar, eliminar, crear,modificar,mostrarDestino,eliminarDestino, crearDestino, modificarDestino

urlpatterns = [
    path('', inicio, name="inicio"),
    path('quienes_somos/', quienes_somos, name='quienes_somos'),
    path('Galeria_imagenes/', Galeria_imagenes, name='Galeria_imagenes'),
    path('Api/', Api, name='Api'),
    path('nuevo_formulario_/', nuevo_formulario_, name='nuevo_formulario_'),
    path('mostrar/', mostrar, name="mostrar"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('crear/',crear, name="crear"),
    path('modificar/<id>', modificar, name="modificar"),
    path('mostrarDestino/', mostrarDestino, name="mostrarDestino"),
    path('eliminarDestino/<id>', eliminarDestino, name="eliminarDestino"),
    path('crearDestino/',crearDestino, name="crearDestino"),
    path('modificarDestino/<id>', modificarDestino, name="modificarDestino"),
]