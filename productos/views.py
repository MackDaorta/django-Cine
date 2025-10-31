from django.shortcuts import render
from .models import Producto


def productos(request):
    productos_list = Producto.objects.all().order_by('categoria', 'nombre')
    context={
        'productos': productos_list
    }
    return render(request, 'productos/productos.html')