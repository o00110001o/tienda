from django.contrib import admin
from django.urls.conf import path
from django.urls import path,include
#from app import admin as appad
from app.views import *
 
urlpatterns = [
    path('', index, name="index"),
    path('home/', home, name="home"),
    path('carrito/', carrito, name="carrito"),
    path('historial/', historial, name="historial"),
    path('productos/', productos,name="productos"),
    path('ingresar/', ingresar,name="login"),
    path('crear_cuenta/', crear_cuenta, name='registration'),
    path('test/', test, name="test"),
#--------------------------------------------------------------------
    path('checkout/', checkout, name="checkout"),
    path('orders/', historial, name="orders"),
    path('successful/', successful, name="successful"),
    path('onprogress/', onprocess, name="onprogress"),
#--------------------------------------------------------------------
    path('agregar/', agregar_producto, name="agregar_productos"),
    path('modificar/', modificar_producto, name="modificar_productos"),
    path('listar/', listar_producto, name="listar_productos"),
]
