from django.db import models
from uuid import uuid4,UUID

class Producto(models.Model):
    CATEGORIAS = [
        ('COMBO', 'Combo'),
        ('POPCORN', 'Popcorn'),
        ('BEBIDA', 'Bebida'),
        ('SNACK','Snack'),
        ('COLECCIONABLES', 'Coleccionables'),
    ]
    id=models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=100, verbose_name='Nombre del Producto')
    
    descripcion= models.TextField(blank=True, null=True, verbose_name='Descripcion')

    precio= models.DecimalField(max_digits=5,decimal_places=2,verbose_name='Precio')

    imagen= models.ImageField(upload_to='productos/',verbose_name='Imagen referencial')

    categoria=models.CharField(max_length=50, choices=CATEGORIAS, default='OTRO', verbose_name='Categoria')
    
    disponible=models.BooleanField(default=True,verbose_name='Disponible')

    def __str__ (self):

        return f"[{self.get_categoria_display()}]  {self.nombre} - S/.{self.precio}"

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

class Anuncio(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre= models.CharField(max_length=100,verbose_name='Nombre del anuncio')
    imagen= models.ImageField(upload_to='anuncios/', verbose_name='anuncios')

    def __str__(self):
        return f'nombre:{self.nombre} id:{self.id}'