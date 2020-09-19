from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


class VistaRegistro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro.html",{"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Esto le indica a la tabla que cree un nuevo usuario por un codigo
            usuario = form.save()
            # Esto toma el dato username que envia viene en form
            # El cleaned_data es para que el valor salga correcto
            nombre = form.cleaned_data.get('username')
            # la f (tambien F) se usa para pasar una variable entre llaves
            messages.success(request, f"Bienvenido {nombre}")
            login(request,usuario)
            return redirect('blog')
        else:
            '''Con este for recorremos todos los mensajes de erro que
            se puedan tener'''
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            return render(request, "registro.html",{"form": form})

def salir(request):
    logout(request),
    messages.success(request, "Sesion cerrada"),
    return redirect('blog')

def acceder(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            usuario = authenticate(username=nombre, password=clave)
            if usuario is not None:
                messages.success(request, f"Bienvenido {nombre}")
                login(request,usuario)
                return redirect('blog')
            else:
                messages.error(request, 'Los datos son incorrectos')    
        else:
            messages.error(request, 'Los datos son incorrectos') 

    form = AuthenticationForm()
    return render(request,'acceder.html',{'form':form})
