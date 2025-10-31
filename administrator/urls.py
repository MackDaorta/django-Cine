from django.urls import path
from . import views  
app_name='administrator'
urlpatterns=[
    path('', views.admin_panel,name='admin_panel'),
    path('productos/', views.admin_productos,name='admin_productos'),
    path('peliculas/',views.admin_peliculas,name='admin_peliculas'),
    path('anuncios/',views.admin_anuncios,name='admin_anuncios' ),
    path('anuncios/eliminar/<uuid:id>/', views.admin_anuncio_eliminar, name='admin_anuncio_eliminar'),
    ###path('anuncios/editar/<uuid:id>/', views.admin_anuncio_editar,name='admin_anuncio_editar'),
    path('productos/eliminar/<uuid:id>/', views.admin_producto_eliminar, name='admin_producto_eliminar'),
    path('productos/editar/<uuid:id>/', views.admin_producto_editar,name='admin_producto_editar'),
    ###path('peliculas/editar/<uuid:id>/', views.admin_pelicula_editar,name='admin_pelicula_editar'),
    ###path('peliculas/eliminar/<uuid:id>/', views.admin_pelicula_eliminar, name='admin_pelicula_eliminar'),
    path('generos/',views.admin_generos,name='admin_generos' ),
    path('salas/',views.admin_salas,name='admin_salas' ),
    ###path('generos/editar/<uuid:id>/', views.admin_genero_editar,name='admin_genero_editar'),
    ###path('generos/eliminar/<uuid:id>/', views.admin_genero_eliminar, name='admin_genero_eliminar'),
    ###path('salas/editar/<uuid:id>/', views.admin_sala_editar,name='admin_sala_editar'),
    ##path('salas/eliminar/<uuid:id>/', views.admin_sala_eliminar, name='admin_sala_eliminar'),
]