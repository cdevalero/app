from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.forms import *
from django.contrib import messages
from blog.models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def hola(request):
    return HttpResponse('hola mundo')

@login_required(login_url="cuentas/acceder/")
def index(request):
    posteos_list = post.objects.all()

    paginator = Paginator(posteos_list, 3)
    # aqui tomamos los datos de la pagina (el numero de pagina url/1)
    # si no temos ningun dato usamos por defecto el 1
    pagina = request.GET.get('page') or 1
    posteos = paginator.get_page(pagina)
    current_page = int(pagina)
    # para que range funcione el ultimo numero simpre tiene que ser +1
    paginas = range (1, posteos.paginator.num_pages +1)

    return render(request,'blog.html', {
        'posts':posteos, 
        'paginas': paginas, 
        'current_page':current_page})

@login_required(login_url="cuentas/acceder/")
def crear_post(request):
    if request.method == 'POST':
        form = FormularioPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor_id = request.user.id
            post.save()
            titulo = form.cleaned_data.get('titulo')
            messages.success(request, f'El post {titulo} se ha creado')
            return redirect('blog')
        else:
            for msg in form.errors_messages:
                messages.error(request, form.error_messages[msg])
            
    form = FormularioPost()
    return render(request, 'crear_post.html', {'form': form})

@login_required(login_url="cuentas/acceder/")
def eliminar_post(request, post_id):
    try:
        posteo = post.objects.get(pk=post_id)
    except post.DoesNotExist:
        # esto se pone para un posteo que no exista
        messages.error(request, 'El post no existe')
        return redirect('blog')

    if posteo.autor != request.user:
        messages.error(request, f'Este post pertenece a {posteo.autor}')
        return redirect('blog')

    posteo.delete()
    messages.success(request, f'El post {posteo.titulo} se elimino con exito')
    return redirect('blog')
