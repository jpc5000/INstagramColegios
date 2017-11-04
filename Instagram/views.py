from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Instagram.models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        email = request.POST['correo']
        name = request.POST['nombre_completo']
        username = request.POST['usuario']
        password = request.POST['password']
        usuarioDjango = User.objects.create_user(username = username, password = password, email=email, first_name = name)
        miUsuario = MiUsuario(usuario_django = usuarioDjango)
        usuarioDjango.save()
        miUsuario.save()
        return redirect ('signin')

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    mi_usuario = MiUsuario.objects.get( pk = request.user.pk)
    context = {'usuario_actual' : request.user}
    return render(request, 'profile.html', context)
