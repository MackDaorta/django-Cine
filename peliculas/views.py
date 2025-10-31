from django.shortcuts import render
from .models import Pelicula

# Create your views here.
def peliculas(request):
    return render(request, 'peliculas/peliculas.html')
