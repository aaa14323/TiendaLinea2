from tienda.models import *
from django.forms import ModelForm

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['cantidadAPagar', 'direccion', 'telefono']

class ClienteForm2(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class CarritoForm(ModelForm):
    class Meta:
        model = Carrito
        fields = '__all__'