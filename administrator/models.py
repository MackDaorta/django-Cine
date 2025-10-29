from django.db import models
from uuid import uuid4

# Create your models here.
class Anuncio(models.Model):
    CATEGORIAS=[
        ('SLIDER','Slider'),
        ('PROMOCION','Promocion')
    ]
    id=models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre= models.CharField(max_length=100,verbose_name='Nombre del anuncio')
    imagen= models.ImageField(upload_to='anuncios/', verbose_name='anuncios')
    tipo=models.CharField(max_length=50,choices=CATEGORIAS,verbose_name='tipo')
    link=models.URLField(max_length=255,blank=True,null=True,verbose_name='Enlace')
    vigencia=models.DateField(blank=True,null=True,verbose_name='Fecha de Vigencia')

    def __str__(self):
        return f'[{self.get_tipo_display()}] {self.nombre}'