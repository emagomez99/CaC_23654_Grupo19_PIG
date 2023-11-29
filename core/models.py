from django.db import models
from django.core.exceptions import ValidationError


class Personaje(models.Model):
    nombre= models.CharField(max_length=50, verbose_name='Nombre')
    anime= models.CharField(max_length=50, verbose_name='Anime/Serie')

    def __str__(self):
        return self.nombre


class Compañia(models.Model):
    nombre= models.CharField(max_length=50, verbose_name='Nombre')
    ubicacion= models.CharField(max_length=50, verbose_name='Ubicación')

    def __str__(self):
        return self.nombre

# RELACION DE UNO A MUCHOS: PERSONAJE - FIGURAS
# RELACION DE MUCHOS A MUCHOS: COMPAÑIAS - FIGURAS
class Figura(models.Model):
    denominacion= models.CharField(max_length=50, verbose_name='Denominación/Nombre')# por omision, los campos son NoNull, para eso sirve poner default=0 (en caso e ya tener datos cargados y querer agregar nuevas columnas)
    personaje= models.ForeignKey(Personaje, on_delete= models.CASCADE) #1 personaje puede tener muchas figuras - me refiero a la tabla Personaje - el on_delete models CASCADE me rompe todo porque si borro Personaje estoy mirando a alg oque no existe si es que lo borro. Entonces on cascade si borro un personaje me lleov puesto todas las figuras que estan asociadas a ese personaje (deberia plantearse al reves la relacion pero no hay tiempo)
    coleccion= models.CharField(max_length=40, verbose_name='Colección/serie')
    compañias= models.ManyToManyField(Compañia) #una compañia produce diversas figuras, y fingimos que muchas compañias producen la misma figura.
    precio= models.FloatField(verbose_name='Precio')
    #fecha_salida= models.DateField(verbose_name= 'Fecha de salida')
    #imagen= models.ImageField(verbose_name= 'Imagen')

    def __str__(self):
        return self.denominacion

'''
    def clean_precio(self): #no me funciona
        if self.cleaned_data['precio'] <= 0:
            raise ValidationError('El precio debe ser un número positivo')
        return self.cleaned_data['precio']
'''   

class Persona(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=150, verbose_name='Apellido')
    email = models.EmailField(max_length=150, verbose_name='Email')
    dni = models.IntegerField(verbose_name='DNI')

class Vendedor(Persona):
    legajo = models.IntegerField(verbose_name='Legajo')
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Administrador(Persona):
    legajo = models.IntegerField(verbose_name='Legajo')
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
