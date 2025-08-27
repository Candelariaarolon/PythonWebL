from django.db import models 

class Workshop(models.Model):
    id = models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to='workshops/', default='workshops/default.jpg')
    Titulo = models.CharField(max_length=200, default='Título predeterminado')
    Tipo = models.CharField(max_length=200, default='Tipo de taller predeterminado')
    Cantidad_personas = models.CharField(max_length=200, default='Cantidad de personas predeterminada')
    Duración = models.CharField(max_length=200, default='Duración predeterminada')
    Descripcion = models.TextField(default='Descripción predeterminada')
    Precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Diseño = models.CharField(max_length=100, default='libre')  # nuevo campo
    Catering = models.BooleanField(default=False)               # nuevo campo

    def __str__(self):
        return self.Titulo
