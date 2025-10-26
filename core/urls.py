from django.urls import path
from . import views  


urlpatterns = [
    path('', views.home, name='home'),
    path('conocenos/', views.conocenos, name='conocenos'),
    path('peliculas/', views.peliculas, name='peliculas'),
    path('productos/', views.productos, name='productos'),
    path('sala/', views.sala, name='sala'),
    path('ubicanos/', views.ubicanos, name='ubicanos'),
    path('login/', views.login, name='login'),
    path('mi-admin/', views.admin_panel,name='admin_panel'),
    path('mi-admin/productos/', views.admin_productos,name='admin_productos'),
    path('mi-admin/peliculas/',views.admin_peliculas,name='admin_peliculas'),
    path('mi-admin/anuncios/',views.admin_anuncios,name='admin_anuncios' ),
    path('logout/', views.logout,name='logout'),
]