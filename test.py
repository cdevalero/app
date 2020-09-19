"""from app.wsgi import *
from blog.models import categoria

unidad = categoria.objects.all()
print(unidad)

'''unidad = categoria(nombre = 'hola')
unidad.save()'''

unidadCategoria = categoria.objects.get(pk=1)
print(unidadCategoria)"""

def test(nombre, *args):
    return nombre, args

nombre, argumento = test("carlos", 22, "varon", True)
print(nombre)
print(type(argumento))
print(argumento)

def test2(nombre, *args, **kwargs):
    return nombre, args, kwargs

nombre, argumento, diccionario = test2("carlos", 22, "varon", vivo=True, nacion="venezuela")
print(type(diccionario))
print(diccionario)
