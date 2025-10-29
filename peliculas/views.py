from django.shortcuts import render

# Create your views here.
def peliculas(request):
    return render(request, 'peliculas/peliculas.html')