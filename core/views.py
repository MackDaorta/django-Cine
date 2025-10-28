from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Anuncio,Peliculas,Producto
from django.urls import reverse
from decimal import Decimal,InvalidOperation

def es_admin(user):
    return user.is_authenticated and user.is_staff

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
    error_message=None
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        descripcion=request.POST.get('descripcion')
        precio_str=request.POST.get('precio')
        imagen=request.FILES.get('imagen')
        categoria=request.POST.get('categoria')
        precio_decimal=None
        try:
            precio_decimal=Decimal(precio_str)
        except(InvalidOperation,TypeError):
            error_message='Ingrese un formato valido'
        if error_message==None:
            try:
                Producto.objects.create(
                    nombre=nombre,
                    descripcion=descripcion,
                    precio=precio_decimal,
                    imagen=imagen,
                    categoria=categoria
                )
                return redirect('admin_productos')
            except Exception as e:
                error_message=f'Error al guardar el producto: {e}'
    productos=Producto.objects.all().order_by('categoria')
    context={
        'productos':productos,
        'error':error_message

    }
    
    return render(request,'core/admin_productos.html',context)

@user_passes_test(es_admin, login_url='/login/')
def admin_peliculas(request):
    
    peliculas=Peliculas.objects.all()
    context={
        'peliculas': peliculas
    }
    return render(request,'core/admin_peliculas.html',context)

@user_passes_test(es_admin, login_url='/login/')
def admin_anuncios(request):
    
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        vigencia=request.POST.get('vigencia')
        tipo=request.POST.get('tipo')
        imagen=request.FILES.get('imagen')
        link=request.POST.get('link')
        if not link:
            link= reverse('productos')
        if not vigencia:
            vigencia= None
        Anuncio.objects.create(
            nombre=nombre,
            tipo=tipo,
            vigencia=vigencia,
            imagen=imagen,
            link=link
            )

        return redirect('admin_anuncios')
    anuncios=Anuncio.objects.all().order_by('tipo')
    context={
        'anuncios':anuncios
    }

    return render(request,'core/admin_anuncios.html',context)


@user_passes_test(es_admin, login_url='/login/')
def admin_anuncio_eliminar(request,id):
    from django.shortcuts import get_object_or_404
    anuncio=get_object_or_404(Anuncio,id=id)
    anuncio.delete()
    return redirect('admin_anuncios')

