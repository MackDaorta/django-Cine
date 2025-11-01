from django.urls import path
from . import views  
app_name='administrator'
urlpatterns=[
    path('', views.admin_panel,name='admin_panel'),
    path('productos/', views.admin_productos,name='admin_productos'),
    path('peliculas/',views.admin_peliculas,name='admin_peliculas'),
    path('anuncios/',views.admin_anuncios,name='admin_anuncios' ),
    path('anuncios/eliminar/<uuid:id>/', views.admin_anuncio_eliminar, name='admin_anuncio_eliminar'),
    path('anuncios/editar/<uuid:id>/', views.admin_anuncios_editar,name='admin_anuncios_editar'),
    path('productos/eliminar/<uuid:id>/', views.admin_producto_eliminar, name='admin_producto_eliminar'),
    path('productos/editar/<uuid:id>/', views.admin_producto_editar,name='admin_producto_editar'),
    path('peliculas/editar/<uuid:id>/', views.admin_peliculas_editar,name='admin_peliculas_editar'),
    path('peliculas/eliminar/<uuid:id>/', views.admin_peliculas_eliminar, name='admin_peliculas_eliminar'),
    path('generos/',views.admin_generos,name='admin_generos' ),
    path('salas/',views.admin_salas,name='admin_salas' ),
    path('generos/editar/<uuid:id>/', views.admin_genero_editar,name='admin_genero_editar'),
    path('generos/eliminar/<uuid:id>/', views.admin_genero_eliminar, name='admin_genero_eliminar'),
    path('salas/editar/<uuid:id>/', views.admin_salas_editar,name='admin_salas_editar'),
    path('salas/eliminar/<uuid:id>/', views.admin_salas_eliminar, name='admin_salas_eliminar'),
]