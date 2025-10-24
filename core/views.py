from django.shortcuts import render

def home(request):
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
    return render(request,'core/login.html')

def adminpanel(request):
    return render(request, 'core/adminpanel.html')