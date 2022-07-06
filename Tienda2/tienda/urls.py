from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adminP/', views.producto_admin, name='producto-admin'),
    path('add/', views.producto_add, name='producto-add'),
    path('delete/<int:idp>', views.delete_producto, name='delete-producto'),
    path('update/<int:idpr>', views.update_producto, name='update-producto'),
    path('compra/', views.lista_compra, name='lista-compra'),
    path('pagar/', views.pagar, name='boton-pagar'),
    path('datosCompra/', views.realizar_compra, name='realizar-compra'),
    path('pagar2/', views.pagarBoton, name='pagarBoton'),
    path('pedidos/', views.pedidos, name='pedidos'),
]