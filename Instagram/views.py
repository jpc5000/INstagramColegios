from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Instagram.models import *


# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        email = request.POST['correo']
        name = request.POST['nombre_completo']
        username = request.POST['usuario']
        password = request.POST['password']
        print (email)
        print (name)
        print (username)
        print (password)
        usuarioDjango = User.objects.create_user(username = username, password = password, first_name = name)
        miUsuario = MiUsuario(usuario_django = usuarioDjango)
        usuarioDjango.save()
        miUsuario.save()
        return redirect ('index')

def index(request):
    print (MiUsuario.objects.count())
    return render(request, 'index.html')
