from django.db import models
from django.core.exceptions import ValidationError

class Personaje(models.Model): #categoria a muchos cursos) ESTE DEBERIA SER CURSO
    nombre= models.CharField(max_length=50, verbose_name='Nombre')
    anime= models.CharField(max_length=50, verbose_name='Anime/Serie')

class Compañia(models.Model):
    nombre= models.CharField(max_length=50, verbose_name='Nombre')
    ubicacion= models.CharField(max_length=50, verbose_name='Ubicación')


class Figura(models.Model):
    denominacion= models.CharField(max_length=50, verbose_name='Denominación/Nombre')# por omision, los campos son NoNull, para eso sirve poner default=0 (en caso e ya tener datos cargados y querer agregar nuevas columnas)
    personaje= models.ForeignKey(Personaje, on_delete= models.CASCADE) #1 personaje puede tener muchas figuras - me refiero a la tabla Personaje - el on_delete models CASCADE me rompe todo porque si borro Personaje estoy mirando a alg oque no existe si es que lo borro. Entonces on cascade si borro un personaje me lleov puesto todas las figuras que estan asociadas a ese personaje (deberia plantearse al reves la relacion pero no hay tiempo)
    coleccion= models.CharField(max_length=40, verbose_name='Colección/serie')
    compañias= models.ManyToManyField(Compañia) #una compañia produce diversas figuras, y fingimos que muchas compañias producen la misma figura.
    precio= models.FloatField(verbose_name='Precio')
    #fecha_salida= models.DateField(verbose_name= 'Fecha de salida')
    #imagen= models.ImageField(verbose_name= 'Imagen')

    '''
    def clean_precio(self): #no me funciona - 23 models 3 - 20:03
        if self.cleaned_data['precio'] > 0:
            raise ValidationError('El precio debe ser un número positivo')
        return self.cleaned_data['precio']
    '''

#defino migraciones, django fijate si hay cosas que cambiaron: 
#python manage.py makemigrations core (se planifican cambios)
#una vez que cree las migraciones, las tengo que aplicar (pasarlas a la BD):
#python manage.py migrate core (se aplican cambios)

#para ir para atras con las migraciones:
#...tore_ocean\store_ocean> python manage.py migrate core 0001_initial

#para arrancar desde cero, osea revertir la primera migracion:
#...l_store_ocean\store_ocean> python manage.py migrate core zero
#ahora puedo borrar las migraciones en la carpeta core>migrations (0001_initial.py y las demas. EL INIT NO LO BORRO Y EL PYCACHE TAMPOCO)


'''
class Compañia(models.Model):
    nombre= models.CharField(max_length=40, verbose_name='Nombre')
    ubicacion= models.CharField(max_length=40, null=True, verbose_name='Ubicación')
    categoria= 
'''