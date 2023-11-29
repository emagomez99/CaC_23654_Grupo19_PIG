from django import forms
from django.core.exceptions import ValidationError
from .models import Personaje, Compañia, Figura  #ChatGPT - revisar pa entender

class GreenBackgroundTextInput(forms.TextInput): #extender un widget para crear uno propio
    class Media:
        CSS = {'all': ('core/css/green_background_text_input.css',)}

class BlueBackgroundTextInput(forms.TextInput):
    class Media:
        CSS = {'all': ('core/css/blue_background_text_input.css',)}

#FORM CON VALIDACIONES EN EL FRONT Y EN EL BACK -----------------------------------------------------------------------------------------------------------------
class ContactoForm(forms.Form): #1:09 21 models 1
    nombre= forms.CharField(label='Nombre de contacto',widget=GreenBackgroundTextInput,required= True) #aca se ponen los placeholders
    apellido= forms.CharField(label='Apellido de contacto', widget=forms.TextInput(attrs= {'class': 'fondo_verde'}),required= True)
    edad= forms.IntegerField(label= 'Edad', widget=GreenBackgroundTextInput)
    mail= forms.EmailField(label='Mail', widget=GreenBackgroundTextInput, required= True)
  
    nombre_pj= forms.CharField(label='Nombre de personaje',widget=BlueBackgroundTextInput,required= True)
    fabricante= forms.CharField(label='Fabricante', widget=BlueBackgroundTextInput)
    coleccion= forms.CharField(label='Serie/Coleccion', widget=BlueBackgroundTextInput)
    mensaje= forms.CharField(label='Descripción', widget=forms.Textarea(attrs= {'class': 'fondo_azul'}))
    #imagen= forms.ImageField(label='Imagen', widget=BlueBackgroundTextInput)

    def clean_edad(self): #validacion a nivel de campo
        #si hay un error, lanzo una excepcion
        if self.cleaned_data['edad'] < 18:
            raise ValidationError("El usuario no puede tener menos de 18 años")
        #sino devuelvo el campo como estaba
        return self.cleaned_data['edad']
    
    def clean(self): #validacion a nivel de form - clean de todo el form, esto valida si lo que me envio el usuario como form completo es valido o no
        #esto simula una busqueda en BD:
        if self.cleaned_data['mail'] == 'c000@gmail.com.ar':
            #si el mail ya existe:
            raise ValidationError("El mail ya se encuentra registrado. Intente con otro mail.") #cualquiera porque el mail es para eque los clientes envien que figura quieren, pero bueno para entener (si registro figuras en el back con un codigo, este ejemplo esta bueno para eso)
        return self.cleaned_data
    

# FORMULARIO ASOCIADO A UN MODELO
class AltaProductoForm(forms.ModelForm): #alta de figura
    denominacion= forms.CharField(label='Denominacion',widget=GreenBackgroundTextInput,required= True)
    personaje = forms.ModelChoiceField(queryset=Personaje.objects.all(), empty_label="Seleccione un Personaje") #ChatGPT - revisar pa entender
    coleccion= forms.CharField(label='Coleccion',widget=GreenBackgroundTextInput,required= True)
    compañias = forms.ModelMultipleChoiceField(queryset=Compañia.objects.all(), widget=forms.CheckboxSelectMultiple) #ChatGPT - revisar pa entender
    precio= forms.FloatField(label='Precio',widget=GreenBackgroundTextInput,required= True)
    #fecha_salida= forms.DateTimeField(label='Fecha de salida',widget=GreenBackgroundTextInput,required= True)
    #imagen= forms.FileField(label='Imagen ilustrativa',widget=GreenBackgroundTextInput,required= True)
    class Meta: #ChatGPT - revisar pa entender
        model = Figura
        fields = '__all__'


class AltaPersonajeForm(forms.Form):
    nombre= forms.CharField(label='Nombre',widget=BlueBackgroundTextInput,required= True)
    anime= forms.CharField(label='Anime/Serie',widget=BlueBackgroundTextInput,required= True)

class AltaEmpresaForm(forms.Form):
    nombre= forms.CharField(label='Nombre',widget=BlueBackgroundTextInput,required= True)
    ubicacion= forms.CharField(label='Pais/región',widget=BlueBackgroundTextInput,required= True)