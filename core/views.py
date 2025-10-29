from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse
from decimal import Decimal,InvalidOperation
from administrator.models import Anuncio




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
    return render(request,'core/sala.html')

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
                return redirect('home')
        else:
            error_message='Usuario o contraseña incorrectos'
    context={
        'error':error_message
    }
    return render(request,'core/login.html',context)

def logout(request):
    auth_logout(request)
    return redirect('home')
