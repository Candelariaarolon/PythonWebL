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
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='ceramica') 
    Diseño = models.CharField(max_length=200, default='Diseño predeterminado')
    Tamaño = models.CharField(max_length=200, default='Tamaño predeterminado')
    Descripcion = models.TextField(default='Descripción predeterminada')
    Precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
 
    def __str__(self):
        return self.Titulo  #Significa que cuando Django (o vos) quiera imprimir ese objeto, lo que va a mostrar es el contenido de self.Titulo, o sea, el título del producto de cerámica.
    

class ProductoImagen(models.Model):
    producto = models.ForeignKey(Producto, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/galeria/')

    

