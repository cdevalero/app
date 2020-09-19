from django import forms
from .models import post

class FormularioPost(forms.ModelForm):
    class Meta:
        model = post;
        fields = ('categoria', 'titulo', 'contenido')

class FormTest(forms.Form):
    name = forms.CharField(max_length=100, empty_value=False)
