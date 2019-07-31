from django.db import models

# Create your models here.
class Producto(models.Model):
    titulo      = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True, null=True)
    precio      = models.DecimalField(decimal_places=2, max_digits=10000)
    resumen     = models.TextField(blank=False, null=False)
    caracteristicas = models.BooleanField()