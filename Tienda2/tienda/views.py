from django.shortcuts import render
from django.http import HttpResponse
from tienda.models import Producto, Cliente, Carrito
from tienda.modelForms import ProductoForm, CarritoForm, ClienteForm

# Create your views here.

def index(request):
    return render(request, 'index.html')


def producto_admin(request):
    p = Producto.objects.all()
    context = {
        'producto': p
    }
    return render(request, 'productos_admin.html', context)

def lista_compra(request):
    pr = Producto.objects.all()
    return render(request, 'lista_compra.html', {'producto': pr})


def producto_add(request):
    if request.method == 'POST':
        formr = ProductoForm(request.POST)
        if formr.is_valid():
            formr.save()
            return producto_admin(request)
    else:
        formset = ProductoForm()
    return render(request, 'producto_add.html', {'mform': formset})

def realizar_compra(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return lista_compra(request)
    else:
        formset = ClienteForm()
    return render(request, 'realizar_compra.html', {'mform': formset})

def delete_producto(request, idp):
    try:
        p1 = Producto.objects.get(id=idp)
        p1.delete()
        return producto_admin(request)
    except:
        print('')
        return producto_admin(request)

def pagar(request):
    if request.method == 'POST':
        formr = CarritoForm(request.POST)
        if formr.is_valid():
            formr.save()
            return lista_compra(request)
    else:
        formset = CarritoForm()
    return render(request, 'boton_pagar.html', {'mform': formset})

def pagarBoton(request):
    cc = Carrito.objects.all()

    return render(request, 'boton_pagar.html', {'carrito': cc})

def update_producto(request, idpr):
    pr1 = Producto.objects.get(id=idpr)
    if request.method == 'GET':
        form = ProductoForm(instance=pr1)
        return render(request, 'update_producto.html', {'mform':form})
    elif request.method == 'POST':
        form = ProductoForm(request.POST, instance=pr1)
        if form.is_valid():
            form.save()
        return producto_admin(request)

def pedidos(request):
    cl = Cliente.objects.all()
    return render(request, 'pedidos.html', {'cliente': cl})