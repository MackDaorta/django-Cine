from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Anuncio,Peliculas,Producto

def es_admin(user):
    return user.is_authenticated and user.is_staff

def home(request):
    lista_sliders=Anuncio.objects.filter(tipo='SLIDER')
    lista_promociones=Anuncio.objects.filter(tipo='PROMOCION')
    context={
        'sliders': lista_sliders,
        'promociones': lista_promociones
    }
    return render(request, 'core/home.html')

def conocenos(request):
    return render(request, 'core/conocenos.html')

def peliculas(request):
    return render(request, 'core/peliculas.html')

def productos(request):
    return render(request, 'core/productos.html')

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
                return redirect('admin_panel')
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

@user_passes_test(es_admin, login_url='/login/')
def admin_panel(request):
    return render(request, 'core/admin_panel.html')

@user_passes_test(es_admin, login_url='/login/')
def admin_productos(request):
    from .models import Producto
    productos=Producto.objects.all()

    context={
        'productos':Producto
    }
    return render(request,'core/admin_productos.html',context)

@user_passes_test(es_admin, login_url='/login/')
def admin_peliculas(request):
    from .models import Peliculas
    peliculas=Peliculas.objects.all()
    context={
        'peliculas': peliculas
    }
    return render(request,'core/admin_peliculas.html',context)

@user_passes_test(es_admin, login_url='/login/')
def admin_anuncios(request):
    from .models import Anuncio
    anuncios=Anuncio.objects.all()
    context={
        'anuncios':anuncios
    } 
    return render(request,'core/admin_anuncios.html',context)


