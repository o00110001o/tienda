import requests #NOS PERMITE LEER EL API
from django.shortcuts import render
from django.forms import *
from django.contrib import messages
from django.contrib.staticfiles import *

from app.forms import ProductoForm
from app.models import Producto

from .models import *
from .forms import *

def index(request):
    return render(request,'index.html')

def home(request):


    return render(request,'home.html')
    
def ingresar(request):
    return render(request, 'login.html')

def crear_cuenta(request):
    return render(request, 'reegistration.html')

def productos(request):
    #response = requests.get('https://rickandmortyapi.com/productos').json()
    productosAll = Producto.objects.all()
    datos = {'listaProductos' : productosAll }
        #'listaJson': response
       
    if request.method == 'POST':
        carrito = Items_Carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.save()
        
    return render(request, 'productos.html')

def carrito(request):
    return render(request, 'carrito.html')
    
def test(request):
    return render(request, 'test.html')

def checkout(request):
    return render(request, 'app/#.html')

def historial(request):
    return render(request, 'historial.html')

def successful(request):
    return render(request, 'app/#.html')

def onprocess(request):
    return render(request, 'app/#.html')

#SECCION LISTAR
def listar_producto(request):
    productoAll = Producto.objects.all()
    datos={
        'listarProductos' : productoAll
    }
    return render(request, 'home.html')

#SECCION AGREGAR
def agregar_producto(request):
    datos = {
        'form' : ProductoForm()
    } 
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'app/agregar_producto.html'
            

    return render(request, 'app/productos/agregar_producto.html')

#SECCION MODIFICAR
def modificar_producto(request, id):
    producto = Producto.objects.get(id=id)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Producto modificado correctamente!'
            datos['form'] = formulario

    return render(request, 'app/productos/modificar_producto.html', datos)

# SECCION ELIMINAR
def eliminar_producto (request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return render(to = 'listar_productos.html')