from django import forms
from .models import post

class FormularioPost(forms.ModelForm):
    class Meta:
        model = post;
        fields = ('categoria', 'titulo', 'contenido')