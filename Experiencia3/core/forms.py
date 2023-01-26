from django import forms
from django.forms import ModelForm 
from django.forms import widgets #permite definir la configuración de los datos de entrada del form
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Cliente, Destino

class ClienteForm(forms.ModelForm):
    
    class Meta: #permite configurar el form 
        model = Cliente 
        fields = ['nro_identif', 'nombreCompleto', 'email', 'telefono', 'destino']
        labels = {
            'nro_identif': 'Rut',
            'nombreCompleto': 'Nombre Completo', ##ojo por el espacio en medio
            'email': 'Email',
            'telefono': 'Telefono',
            'destino': 'Nombre Destino',
        }
        widgets={
            'nro_identif': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite un RUT',
                    'id': 'nro_identif'
                }
            ),
            'nombreCompleto': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Digite su nombre completo',
                    'id': 'nombreCompleto'
                }
            ),
            'email': forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder': 'Digite su email',
                    'id': 'email'
                }
            ),
            'telefono': forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder': 'Digite su telefono',
                    'id': 'telefono'
                }
            ),
            'destino':forms.Select(
                attrs = {
                    'class': 'form-control',
                    'id': 'destino'
                }
            ),
        }

class DestinoForm(forms.ModelForm):
    
    class Meta: #permite configurar el form 
        model = Destino 
        fields = ['cod_des', 'nombre_des', 'precio', 'imagen']
        labels = {
            'cod_des': 'Codigo',
            'nombre_des': 'Nombre del Destino', ##ojo por el espacio en medio
            'precio': 'Precio',
            'imagen': 'Imagen'
        }
        widgets={
            'cod_des': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Codigo del destino',
                    'id': 'cod_des'
                }
            ),
            'nombre_des': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Digite un destino a viajar',
                    'id': 'nombre_des'
                }
            ),
            'precio': forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder': 'Ingrese un precio del destino',
                    'id': 'precio'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen',
                }
            )
        }

