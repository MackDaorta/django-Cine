from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from decimal import Decimal,InvalidOperation
from productos.models import Producto
from peliculas.models import Pelicula, Genero, Sala
from .models import Anuncio


### Funcion que verifica administrador
def es_admin(user):
    return user.is_authenticated and user.is_staff
### Vista administrador
@user_passes_test(es_admin, login_url='/login/')
def admin_panel(request):
    return render(request, 'administrator/admin_panel.html')

### CRUD PRODUCTOS

@user_passes_test(es_admin, login_url='/login/')
def admin_productos(request):
    error_message = None
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio_str = request.POST.get('precio')
        imagen = request.FILES.get('imagen')
        categoria = request.POST.get('categoria')
        precio_decimal = None
        
        try:
            precio_decimal = Decimal(precio_str)
        except (InvalidOperation, TypeError, ValueError):
            error_message = 'Ingrese un formato valido para el precio.'

        if error_message is None:
            if not imagen:
                error_message = 'Debe subir una imagen.'
            elif not categoria:
                error_message = 'Debe seleccionar una categoría.'

        if error_message is None:
            try:
                Producto.objects.create(
                    nombre=nombre,
                    descripcion=descripcion,
                    precio=precio_decimal,
                    imagen=imagen,
                    categoria=categoria
                )
                return redirect('administrator:admin_productos')
            except Exception as e:
                error_message = f'Error al guardar el producto: {e}'


    productos = Producto.objects.all().order_by('categoria')
    context = {
        'productos': productos,
        'error': error_message
    }
    return render(request, 'administrator/admin_productos.html', context)
@user_passes_test(es_admin, login_url='/login/')
def admin_producto_editar(request,id):
    producto = get_object_or_404(Producto,id=id)
    error_message=None # Inicializa
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        descripcion=request.POST.get('descripcion')
        precio_str=request.POST.get('precio')
        categoria=request.POST.get('categoria')
        imagen_nueva=request.FILES.get('imagen')
        precio_decimal=None
        
        
        try: 
            precio_decimal=Decimal(precio_str)
        except (InvalidOperation,TypeError,ValueError):
            error_message='Ingrese un formato valido para el precio.'

    
        if error_message==None:
            try:
                producto.nombre=nombre
                producto.descripcion=descripcion
                producto.precio=precio_decimal
                producto.categoria=categoria
                
                if imagen_nueva:
                    producto.imagen=imagen_nueva
                    
                producto.save()
                return redirect('administrator:admin_productos') 
            except Exception as e:
                error_message=f'Error al editar el producto: {e}'
                
    context={
        'producto':producto,
        'error':error_message
    }
    return render(request,'administrator/admin_producto_editar.html',context)
@user_passes_test(es_admin, login_url='/login/')
def admin_producto_eliminar(request,id):
    producto=get_object_or_404(Producto,id=id)
    if request.method=='POST':
        producto.delete()
        return redirect('administrator:admin_productos')
    return redirect('administrator:admin_productos')
###CRUD SALAS
@user_passes_test(es_admin, login_url='/login/')
def admin_salas(request):
    error_message=None
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        descripcion=request.POST.get('descripcion')
        imagen=request.FILES.get('imagen')
        if not imagen:
            error_message='Ingrese una imagen'
        elif Sala.objects.filter(nombre=nombre).exists():
            error_message='La sala ya existe'
        if error_message==None:
            try:
                Sala.objects.create(
                    nombre=nombre,
                    descripcion=descripcion,
                    imagen=imagen
                )
                return redirect('administrator:admin_salas')
            except Exception as e:
                error_message=f'Error al guardar la sala: {e}'
    salas=Sala.objects.all()
    context={
        'salas':salas,
        'error':error_message
    }
    return render(request,'administrator/admin_salas.html',context)

@user_passes_test(es_admin, login_url='/login/')
def admin_salas_editar(request,id):
    sala = get_object_or_404(Sala,id=id)
    error_message=None
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        descripcion=request.POST.get('descripcion')
        imagen_nueva=request.FILES.get('imagen')
        if error_message==None:
            try:
                sala.nombre=nombre
                sala.descripcion=descripcion
                if imagen_nueva:
                    sala.imagen=imagen_nueva
                sala.save()
                return redirect('administrator:admin_salas')
            except Exception as e:
                error_message=f'Error al editar la sala: {e}'
    context={
        'sala':sala,
        'error':error_message
    }
    return render(request,'administrator/admin_salas_editar.html',context)
@user_passes_test(es_admin, login_url='/login/')
def admin_salas_eliminar(request,id):
    sala=get_object_or_404(Sala,id=id)
    if request.method=='POST':
        sala.delete()
        return redirect('administrator:admin_salas')
    return redirect('administrator:admin_salas')



### CRUD PELICULAS
@user_passes_test(es_admin, login_url='/login/')
def admin_peliculas(request):
    error_message=None
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        sinopsis=request.POST.get('sinopsis')
        restriccion=request.POST.get('restriccion')
        duracion_str=request.POST.get('duracion')
        fecha_estreno=request.POST.get('fecha_estreno')
        imagen=request.FILES.get('imagen')
        generos=request.POST.getlist('generos')
        salas=request.POST.getlist('salas')
        duracion_minutos=None
        try:
            duracion_minutos=int(duracion_str)
            if not imagen:
                error_message='Ingrese una imagen'
            elif not generos:
                error_message='Seleccione al menos un genero'
        except (ValueError,TypeError):
            error_message='Ingrese un formato valido para la duracion'
        if error_message==None:
            try:
                pelicula=Pelicula.objects.create(
                    nombre=nombre,
                    sinopsis=sinopsis,
                    restriccion=restriccion,
                    duracion_minutos=duracion_minutos,
                    fecha_estreno=fecha_estreno,
                    imagen=imagen
                )
                pelicula.generos.set(generos)
                pelicula.salas.set(salas)
                return redirect('administrator:admin_peliculas')
            except Exception as e:
                error_message=f'Error al guardar la pelicula: {e}'
    peliculas=Pelicula.objects.all().order_by('nombre')
    generos=Genero.objects.all()
    salas=Sala.objects.all()
    context={
        'peliculas':peliculas,
        'generos':generos,
        'salas':salas,
        'error':error_message
    }
    return render(request,'administrator/admin_peliculas.html',context)

@user_passes_test(es_admin, login_url='/login/')
def admin_peliculas_editar(request,id):
    error_message=None
    pelicula = get_object_or_404(Pelicula,id=id)
    
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        sinopsis=request.POST.get('sinopsis') 
        restriccion=request.POST.get('restriccion')
        generos_ids=request.POST.getlist('generos')
        salas_ids=request.POST.getlist('salas')
        duracion_str=request.POST.get('duracion_minutos') 
        imagen_nueva=request.FILES.get('imagen')
        
        duracion_minutos=None
        try:
            duracion_minutos=int(duracion_str)
        except (ValueError,TypeError):
            error_message='Ingrese un formato valido para la duracion'
        
        if error_message==None:
            try:
                pelicula.nombre=nombre
                pelicula.sinopsis=sinopsis 
                pelicula.duracion_minutos=duracion_minutos 
                pelicula.restriccion=restriccion
                pelicula.generos.set(generos_ids)
                pelicula.salas.set(salas_ids)

                if imagen_nueva:
                    pelicula.imagen=imagen_nueva
                pelicula.save()

                return redirect('administrator:admin_peliculas')
            except Exception as e:
                error_message=f'Error al editar la pelicula: {e}'
    
    
    generos = Genero.objects.all()
    salas = Sala.objects.all()
    context={
        'pelicula':pelicula, 
        'generos': generos,
        'salas': salas,
        'error':error_message
    }
    return render(request,'administrator/admin_peliculas_editar.html',context)

@user_passes_test(es_admin, login_url='/login/')
def admin_peliculas_eliminar(request,id):
    pelicula=get_object_or_404(Pelicula,id=id)
    if request.method=='POST':
        pelicula.delete()
        return redirect('administrator:admin_salas')
    return redirect('administrator:admin_salas')

### CRUD GENEROS
@user_passes_test(es_admin, login_url='/login/')
def admin_generos(request):
    error_message=None
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        descripcion=request.POST.get('descripcion')
        if not nombre:
            error_message='Ingrese un nombre'
        elif Genero.objects.filter(nombre=nombre).exists():
            error_message='El genero ya existe'
        if error_message==None:
            try:
                Genero.objects.create(
                    nombre=nombre,
                    descripcion=descripcion
                )
                return redirect('administrator:admin_generos')
            except Exception as e:
                error_message=f'Error al guardar el genero: {e}'
    generos=Genero.objects.all().order_by('nombre')
    context={
        'generos':generos,
        'error':error_message
    }
    return render(request,'administrator/admin_generos.html',context)

@user_passes_test(es_admin, login_url='/login/')
def admin_genero_editar(request,id):
    error_message=None
    generos = get_object_or_404(Genero,id=id)
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        descripcion=request.POST.get('descripcion')
        if error_message==None:
            try:
                generos.nombre=nombre
                generos.descripcion=descripcion
                generos.save()
                return redirect('administrator:admin_generos')
            except Exception as e:
                error_message=f'Error al editar el genero: {e}'
    context={
        'generos':generos,
        'error':error_message
    }
    return render(request,'administrator/admin_genero_editar.html',context)


@user_passes_test(es_admin, login_url='/login/')
def admin_genero_eliminar(request,id):
    genero=get_object_or_404(Genero,id=id)
    if request.method=='POST':
        genero.delete()
        return redirect('administrator:admin_generos')
    return redirect('administrator:admin_generos')


### CRUD ANUNCIOS
@user_passes_test(es_admin, login_url='/login/')
def admin_anuncios(request):
    error_message=None
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        vigencia=request.POST.get('vigencia')
        tipo=request.POST.get('tipo')
        imagen=request.FILES.get('imagen')
        link=request.POST.get('link')
        link_final=link
        if not link:
            try:
                link_final= reverse('productos:productos')
            except Exception:
                link_final=None
                error_message='Ingrese un enlace valido'
        if not vigencia:
            vigencia= None
        if error_message==None:
            if not imagen:
                    error_message='Ingrese una imagen'
            else:
                try:
                    Anuncio.objects.create(
                        nombre=nombre,
                        tipo=tipo,
                        vigencia=vigencia,                            imagen=imagen,
                        link=link
                        )
                    return redirect('administrator:admin_anuncios')
                except Exception as e:
                    error_message=f'Error al guardar el anuncio: {e}'
    anuncios=Anuncio.objects.all().order_by('tipo')
    context={
        'anuncios':anuncios,
        'error':error_message
    }

    return render(request,'administrator/admin_anuncios.html',context)

@user_passes_test(es_admin, login_url='/login/')
def admin_anuncios_editar(request,id):
    anuncio = get_object_or_404(Anuncio,id=id)
    error_message=None 
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        tipo=request.POST.get('tipo')
        link=request.POST.get('link')
        vigencia=request.POST.get('vigencia')
        imagen_nueva=request.FILES.get('imagen')
        if error_message==None:
            try:
                anuncio.nombre=nombre
                anuncio.tipo=tipo
                anuncio.link=link
                anuncio.vigencia=vigencia
                
                if imagen_nueva:
                    anuncio.imagen=imagen_nueva
                    
                anuncio.save()
                return redirect('administrator:admin_anuncios') 
            except Exception as e:
                error_message=f'Error al editar el anuncio: {e}'
                
    context={
        'anuncio':anuncio,
        'error':error_message
    }
    return render(request,'administrator/admin_anuncios_editar.html',context)


@user_passes_test(es_admin, login_url='/login/')
def admin_anuncio_eliminar(request,id):
    anuncio=get_object_or_404(Anuncio,id=id)
    if request.method=='POST':
        anuncio.delete()
        return redirect('administrator:admin_anuncios')
    return redirect('administrator:admin_anuncios')



