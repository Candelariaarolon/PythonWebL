from django.db import models

class Productopago(models.Model):
    Titulo = models.CharField(max_length=100)
    Precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Titulo
