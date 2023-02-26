from django.db import models
from datetime import datetime #tiempo

# Create your models here.

class Categoria(models.Model): # Disiplina 
    nombre = models.CharField(max_length=10, unique=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# Datos De La Nueva Instalacion

class Tipospq(models.Model):# Instalacion
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.CharField(max_length=200)
    restriciones = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='imagenes/tipospqs/%Y/%m/%d/')
    estado = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre

# opciones_horaInicio
opciones_Presentaciones = [
    [0,'..........'],
    [1,'500g'],
    [2,'1kg'],
    [3,'2kg'],
    [4,'5kg'],
    [5,'10kg'],
    [6,'25kg'],
    [7,'50kg'],
    [8,'Stick Packs'],
]
# opciones_horaFin
opciones_Productos = [
    (0,'..........'),
    (1,'Azucar Blanca'),
    (2,'Azucar Morena'),
    (3,'Azucar Ligero'),
    (4,'Azucar Turbinado'),
    (5,'Azucar Blanco Organico'),
    (6,'Azucar De Coco Organico'),
    (7,'Panela'),
    (8,'Steviazucar Blanca'),
    (9,'Steviazucar Morena'),
    (10,'Stevia Panela'),

]


class Lista(models.Model): # Reserva
    id_tipospq = models.ForeignKey(Tipospq, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    cedula = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    fecha_creacion = models.DateField(default=datetime.now)
    fecha_compra = models.DateField()
    # codigo_qr = models.CharField(max_length=255, unique=True)
    cantidad = models.CharField(max_length=10)
    Presentaciones = models.IntegerField(choices=opciones_Presentaciones)
    Productos = models.IntegerField(choices=opciones_Productos)   
    estado = models.BooleanField(default=True)