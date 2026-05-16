from django.db import models
from django.contrib.auth.models import User


class Producto(models.Model):
    id= models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to='productos/', default='productos/default.jpg')
    Titulo = models.CharField(max_length=200, default='Título predeterminado')
    TIPO_CHOICES = [
        ('ceramica', 'Cerámica'),
        ('acuarelas', 'Acuarelas'),
        ('cuadros', 'Cuadros'),
        ('wedding', 'Wedding'),
        ('personalizado', 'Personalizado'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='ceramica')

    COLECCION_CHOICES = [
        ('limones', 'Limones'),
        ('morrisyco', 'Morris&Co'),
        ('olivos', 'Olivos'),
        ('magnolias', 'Magnolias'),
        ('cerezos', 'Cerezos'),
        ('mediterraneo', 'Mediterráneo'),
    ]
    coleccion = models.CharField(max_length=20, choices=COLECCION_CHOICES, blank=True, null=True, verbose_name='Colección')
    destacado = models.BooleanField(default=False, help_text='Aparece en la sección Best Sellers')
    Diseño = models.CharField(max_length=200, default='Diseño predeterminado')
    Tamaño = models.CharField(max_length=200, default='Tamaño predeterminado')
    Descripcion = models.TextField(default='Descripción predeterminada')
    Precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    descuento = models.PositiveSmallIntegerField(default=0, help_text='Porcentaje de descuento (0-100)')
    stock = models.PositiveIntegerField(default=0)

    @property
    def precio_final(self):
        if self.descuento:
            return round(self.Precio * (1 - self.descuento / 100), 2)
        return self.Precio

    @property
    def tiene_descuento(self):
        return self.descuento > 0

    def __str__(self):
        return self.Titulo
    

class ProductoImagen(models.Model):
    producto = models.ForeignKey(Producto, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/galeria/')

    

