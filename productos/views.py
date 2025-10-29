from django.shortcuts import render


def productos(request):
    return render(request, 'productos/productos.html')