from django.db import models
from uuid import uuid4

class Sala(models.Model):
    nombre=models.CharField(max_length=10, verbose_name='Nombre de la Sala',unique=True)
    descripcion=models.TextField(blank=True, verbose_name='Descripcion')
    imagen=models.ImageField(upload_to='salas/',verbose_name='Imagen')

    def __str__(self):
        return self.nombre
    
class Genero(models.Model):
    nombre=models.CharField(max_length=50, verbose_name='Nombre del Genero',unique=True)
    descripcion=models.TextField(blank=True, verbose_name='Descripcion')

    def __str__(self):
        return self.nombre




class Pelicula(models.Model):
    RESTRICCION = [
        ('APT','APT'),
        ('+14','+14'),
        ('+18','+18'),
    ]
    id=models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre= models.CharField(max_length=100, verbose_name='Nombre de la Pelicula')

    sinopsis=models.TextField(blank=True, verbose_name='Descripcion')

    imagen= models.ImageField(upload_to='peliculas/',verbose_name='Imagen')

    restriccion=models.CharField(max_length=30, choices=RESTRICCION,verbose_name='restriccion')
    salas=models.ManyToManyField(Sala,verbose_name='Sala')
    generos=models.ManyToManyField(Genero,verbose_name='Genero')
    duracion_minutos=models.PositiveIntegerField(verbose_name='Duracion en minutos')
    fecha_estreno=models.DateField(verbose_name='Fecha de estreno')

    def __str__(self):
        return f'{self.nombre} ({self.restriccion}) '
    
    def get_duracion_formateada(self):
        if self.duracion_minutos:
            horas=self.duracion_minutos//60
            minutos=self.duracion_minutos%60
            return f'{horas}h {minutos}m'
        return 'N/A'