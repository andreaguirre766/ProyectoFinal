from django.contrib import admin
from django.urls import path
from Blog.views import listar_zapatillas , info_marca , agregar_comentario , eliminar_comentario




urlpatterns = [
    path("zapatillas/", listar_zapatillas, name="lista_zapatillas" ),
    path("infomarca/", info_marca , name="info_marca"),
    path('comentarios/', agregar_comentario, name='comentarios'),
     path('comentarios/eliminar/<int:comentario_id>/', eliminar_comentario, name='eliminar_comentario'),
    
     ]
