from django import forms
from django.core.exceptions import ValidationError
from .models import Personaje, Compañia, Figura

class GreenBackgroundTextInput(forms.TextInput): #extender un widget para crear uno propio
    class Media:
        CSS = {'all': ('core/css/green_background_text_input.css',)}

class BlueBackgroundTextInput(forms.TextInput):
    class Media:
        CSS = {'all': ('core/css/blue_background_text_input.css',)}

#FORM CON VALIDACIONES EN EL FRONT Y EN EL BACK -----------------------------------------------------------------------------------------------------------------
class ContactoForm(forms.Form): #1:09 21 models 1
    nombre = forms.CharField(label='Nombre de contacto',widget=forms.TextInput(attrs={'class': 'form-control'}),required= True) #aca se ponen los placeholders
    apellido = forms.CharField(label='Apellido de contacto', widget=forms.TextInput(attrs={'class': 'form-control'}),required= True)
    edad = forms.IntegerField(label= 'Edad', widget=forms.TextInput(attrs={'class': 'form-control'}))
    mail = forms.EmailField(label='Mail', widget=forms.EmailInput(attrs={'class': 'form-control'}), required= True)

    nombre_pj= forms.CharField(label='Nombre de personaje',widget=forms.TextInput(attrs={'class': 'form-control'}),required= True)
    fabricante= forms.CharField(label='Fabricante', widget=forms.TextInput(attrs={'class': 'form-control'}))
    coleccion= forms.CharField(label='Serie/Coleccion', widget=forms.TextInput(attrs={'class': 'form-control'}))
    mensaje= forms.CharField(label='Descripción', widget=forms.Textarea(attrs= {'class': 'form-control'}))
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
class AltaFiguraForm(forms.ModelForm): #alta de figura
    denominacion= forms.CharField(label='Denominacion',widget=forms.TextInput(attrs={'class': 'form-control'}),required= True)
    personaje = forms.ModelChoiceField(queryset=Personaje.objects.all(), empty_label="Seleccione un Personaje") #ChatGPT - revisar pa entender
    coleccion= forms.CharField(label='Coleccion',widget=forms.TextInput(attrs={'class': 'form-control'}),required= True)
    compañias = forms.ModelMultipleChoiceField(queryset=Compañia.objects.all(), widget=forms.CheckboxSelectMultiple) #ChatGPT - revisar pa entender
    precio= forms.FloatField(label='Precio',widget=forms.TextInput(attrs={'class': 'form-control'}),required= True)
    #fecha_salida= forms.DateTimeField(label='Fecha de salida',widget=forms.TextInput(attrs={'class': 'form-control'}),required= True)
    #imagen= forms.FileField(label='Imagen ilustrativa',widget=forms.TextInput(attrs={'class': 'form-control'}),required= True)
    class Meta: #ChatGPT - revisar pa entender
        model = Figura
        fields = '__all__'


class AltaPersonajeForm(forms.Form):
    nombre= forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'class': 'form-control'}),required= True)
    anime= forms.CharField(label='Anime/Serie',widget=forms.TextInput(attrs={'class': 'form-control'}),required= True)

class AltaCompañiaForm(forms.Form):
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    ubicacion= forms.CharField(label='Pais/región',widget=forms.TextInput(attrs={'class': 'form-control'}),required= True)