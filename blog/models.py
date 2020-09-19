from django.db import models
from django.contrib.auth.models import User

class categoria(models.Model):
    #la PK la genera Django automaticamente
    nombre = models.CharField(max_length=100, null=False, unique=True, verbose_name='Nombre')

    # Nos permite convertir este objeto en una cadena pasando el nombre
    def __str__(self):
        return self.nombre
    
    # define los meta datos de la tabla, nombre, orden, etc
    class Meta:
        # cambia el nombre de la tabla del por defecto a categories
        db_table = 'categories'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        # ordenar asendentemente (desendente es -id)
        ordering = ['id']

class post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, unique=True, null=False, verbose_name='Titulo')
    contenido = models.TextField(null=True, verbose_name='Contenido del post')
    # imagen = models.ImageField(upload_to='posts/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen del post')
    fecha_alta = models.DateTimeField(auto_now_add=True, verbose_name='Fecha alta')
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha actualizacion')

    def __str__(self):
        return self.titulo
        
    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']

class Test(models.Model):
    # Definicion de los parametros de las columnas de la tabla
    name = models.CharField(max_length=100, null=False, unique=True, verbose_name='Name')

    # Definicion de que queremos que se retorne cuando se llame a Test en fron, en este caso un sting
    def __str__(self):
        return self.name

    # Definicion de de los Meta-datos de la tabla en BD
    class Meta:
        # nombre de la tabal
        db_table = 'formtest'
        # nombres para la vista de admin
        verbose_name = 'Formtest'
        verbose_name_plural = 'Formtests'
        # orden de vizualizacion (para migraciones)
        ordering = ['id']