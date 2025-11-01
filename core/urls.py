from django.urls import path
from . import views  

app_name='core'
urlpatterns = [
    path('', views.home, name='home'),
    path('conocenos/', views.conocenos, name='conocenos'),
    path('sala/', views.sala, name='sala'),
    path('ubicanos/', views.ubicanos, name='ubicanos'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout,name='logout'),
    path('registro/', views.vista_registro, name='registro'),
]