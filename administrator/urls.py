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
]