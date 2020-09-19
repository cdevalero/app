from django import forms
from .models import *

class FormularioPost(forms.ModelForm):
    class Meta:
        model = post;
        fields = ('categoria', 'titulo', 'contenido')
    
class FormTest(forms.ModelForm):
    class Meta:
        # importamos la clase que estamos usando en models
        model = Test;
        # fields son los campos que vamos a mostrar para trabajar con ellos en front
        # fields es una tupla, por lo tanto no acepta un solo dato
        fields = ('name',)


