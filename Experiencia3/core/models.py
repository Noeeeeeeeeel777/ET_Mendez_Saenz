from django.db import models

# Create your models here.



class Destino(models.Model):
    cod_des= models.IntegerField(primary_key=True, verbose_name='Codigo Destino') 
    nombre_des=models.CharField(max_length=55, verbose_name='Nombre Destino')
    precio=models.IntegerField(max_length=6, verbose_name='Precio')
    imagen=models.ImageField(upload_to="imagenes", null=True, verbose_name='Imagen')  #la img

    def __str__(self):
        return self.nombre_des

class Cliente(models.Model):
    nro_identif=models.CharField(max_length=15, primary_key=True, verbose_name='Rut')
    nombreCompleto=models.CharField(max_length=40, verbose_name='Nombre Completo')
    email=models.CharField(max_length=40, verbose_name='Email')
    telefono=models.IntegerField(max_length=9, verbose_name='Telefono')
    destino=models.ForeignKey(Destino, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreCompleto


        