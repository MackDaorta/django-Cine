from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.urls import reverse
from decimal import Decimal,InvalidOperation
from administrator.models import Anuncio
from peliculas.models import Sala




def home(request):
    lista_sliders=Anuncio.objects.filter(tipo='SLIDER')
    lista_promociones=Anuncio.objects.filter(tipo='PROMOCION')
    context={
        'sliders': lista_sliders,
        'promociones': lista_promociones
    }
    return render(request, 'core/home.html',context)

def conocenos(request):
    return render(request, 'core/conocenos.html')

def sala(request):
    lista_salas=Sala.objects.all()
    context={
        'salas':lista_salas
    }
    return render(request,'core/sala.html',context)

def ubicanos(request):
    return render(request,'core/ubicanos.html')

def login(request):
    error_message = None
    if request.method=='POST':
        username_data=request.POST.get('username')
        password_data=request.POST.get('password')

        user= authenticate(request,username=username_data,password=password_data)
        if user is not None:
            auth_login(request,user)
            if user.is_staff:
                return redirect('administrator:admin_panel')
            else:
                return redirect('core:home')
        else:
            error_message='Usuario o contraseña incorrectos'
    context={
        'error':error_message
    }
    return render(request,'core/login.html',context)

def logout(request):
    auth_logout(request)
    return redirect('core:home')

def vista_registro(request):
    error_message = None

    if request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email', '') 
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            error_message = "Las contraseñas no coinciden."
        elif len(password) < 8: 
            error_message = "La contraseña debe tener al menos 8 caracteres."
        elif not username:
            error_message = "El nombre de usuario no puede estar vacío."

        if error_message is None:
            try:

                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )

                return redirect('core:login') 
            
            except IntegrityError:
                error_message = "El nombre de usuario ya está registrado."
            except Exception as e:
                error_message = f"Error desconocido al registrar: {e}"

    context = {
        'error': error_message
    }
    return render(request, 'core/registro.html', context)