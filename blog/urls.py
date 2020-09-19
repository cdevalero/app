from django.urls import path
from .views import *

urlpatterns = [
    path('hola-mundo/', hola, name="hola"),
    path('',index, name="blog"),
    path('post/crear/',crear_post, name="crear_post"),
    # pasamos un parametro tipo int llamado post_id
    path('post/eliminar/<int:post_id>',eliminar_post, name="eliminar_post"),

    path('testform/',testform, name="testform"),
    path('show_form/',show_form, name="show_form"),
    path('eliminar_test/<int:test_id>',borrar_test, name="borrar_test"),
    path('alter_test/<int:test_id>',alter_test, name="alter_test"),
]


