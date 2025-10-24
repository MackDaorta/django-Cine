from django.urls import path
from . import views  


urlpatterns = [
    path('', views.home, name='home'),
    path('conocenos/', views.conocenos, name='conocenos'),
    path('peliculas/', views.peliculas, name='peliculas'),
    path('productos/', views.productos, name='productos'),
    path('sala/', views.sala, name='sala'),
    path('ubicanos/', views.ubicanos, name='ubicanos'),
    path('adminpanel/', views.adminpanel, name='adminpanel'),
    path('login/', views.login, name='login'),
]