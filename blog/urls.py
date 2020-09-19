from django.urls import path
from .views import *

urlpatterns = [
    path('hola-mundo/', hola, name="hola"),
    path('',index, name="blog"),
    path('post/crear/',crear_post, name="crear_post"),
    # pasamos un parametro tipo int llamado post_id
    path('post/eliminar/<int:post_id>',eliminar_post, name="eliminar_post"),
]


