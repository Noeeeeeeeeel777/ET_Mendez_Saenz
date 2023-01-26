from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm
from .models import Destino
from .forms import DestinoForm
#falta ojo

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def Galeria_imagenes(request):
    return render(request, 'Galeria_imagenes.html')

def Api(request):
    return render(request, 'Api.html')

def nuevo_formulario_(request):
    return render(request, 'nuevo_formulario_.html')


def mostrar(request):
    #obtenemos todos los clientes almacenados en la clase
    clientes = Cliente.objects.all()
    #creamos un diccionario
    datos={
        'consumidores':clientes
    }
    #devolvemos a un template el diccionario y su contenido
    return render(request, 'mostrar.html', datos)
    
def eliminar(request, id):
    cliente = Cliente.objects.get(nro_identif=id)
    cliente.delete()
    return redirect('mostrar')

def crear(request):
    if request.method=='POST': 
        clienteform = ClienteForm(request.POST)
        if clienteform.is_valid():
            clienteform.save()     #similar al insert
            return redirect('mostrar')
    else:
        clienteform=ClienteForm()
    return render(request, 'crear.html', {'clienteform': clienteform})


def modificar(request, id):
    cliente = Cliente.objects.get(nro_identif=id) 
    datos ={
        'form': ClienteForm(instance=cliente) 
    }
    if request.method=='POST':
        formulario = ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrar')
    return render(request, 'modificar.html', datos)

#falta el otro crud para la clase destino * * * * * * * * * * * * * * 

def mostrarDestino(request):
    #obtenemos todos los destinos almacenados en la clase
    destino = Destino.objects.all()
    #creamos un diccionario
    datos={
        'sitios':destino #- - - - - - - - - - > palabra clave diccionario
    }
    #devolvemos a un template el diccionario y su contenido
    return render(request, 'mostrarDestino.html', datos)
    
def eliminarDestino(request, id):
    destino = Destino.objects.get(cod_des=id)
    destino.delete()
    return redirect('mostrarDestino')

def crearDestino(request):
    if request.method=='POST': 
        destinoform = DestinoForm(request.POST, request.FILES)
        if destinoform.is_valid():
           destinoform.save()     #similar al insert
           return redirect('mostrarDestino')
    else:
        destinoform=DestinoForm()
    return render(request, 'crearDestino.html', {'destinoform': destinoform})


def modificarDestino(request, id):
    destino = Destino.objects.get(cod_des=id) 
    datos ={
        'form': DestinoForm(instance=destino) 
    }
    if request.method=='POST':
        formulario = DestinoForm(data=request.POST, instance=destino)
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrar')
    return render(request, 'modificarDestino.html', datos)
