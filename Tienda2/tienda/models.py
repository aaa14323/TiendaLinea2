from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=25, null=True)
    imagen = models.ImageField(upload_to='images/', null=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    piezas = models.IntegerField(null=True)
    
    def __str__(self):
        return '{0},{1},{2}'.format(self.nombre, self.imagen, self.precio, self.piezas)


class Carrito(models.Model):
    producto = models.ManyToManyField(Producto)
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return '{0},{1}'.format(self.total, self.cantidadAPagar)


class Cliente(models.Model):
    producto =  models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    carrito = models.ForeignKey(Carrito, on_delete=models.SET_NULL, null=True)
    cantidadAPagar = models.IntegerField(null=True) #cantidad que da el cliente para pagar
    direccion = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return '{0},{1},{2}'.format(self.cantidadAPagar, self.direccion, self.telefono)