from django.db import models
from uuid import uuid4



class Peliculas(models.Model):
    RESTRICCIONES = [
        ('APT','APT'),
        ('+14','+14'),
        ('+18','+18'),
    ]
    id=models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre= models.CharField(max_length=100, verbose_name='Nombre de la Pelicula')

    descripcion=models.TextField(blank=True, verbose_name='Descripcion')

    imagen= models.ImageField(upload_to='peliculas/',verbose_name='Imagen')

    restricciones=models.CharField(max_length=30, choices=RESTRICCIONES,verbose_name='restricciones')

    def __str__(self):
        return f'{self.nombre} ({self.restricciones}) '