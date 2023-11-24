from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactoForm, AltaProductoForm, AltaPersonajeForm, AltaEmpresaForm
from django.urls import reverse
from django.contrib import messages
from .models import Figura, Personaje, Compañia


def index(request):
    return render(request, 'core/index.html')

def contacto(request): #checkear 21 models 1 - 1:09

    #print(request.POST) #aca tengo todo lo que envio el user en forma de diccionario
    if request.method == "POST": #si el metodo por el cual me enviaron el form es un post
        #instanciar el form con los datos que se cargaron
        formulario= ContactoForm(request.POST) #creamos form y le paso los datos del post, me permite validarlo despues
        
        #valido el form cargado ()
        if formulario.is_valid(): #si el form es valido se corre ValidationError, se hace una conversion de lo que viene del request a tipos de daots que maneja python (strings, etc)
            #dar de alta la info (esto esta pendiente para cuando tengas BD)
            #redirecciono al inicio para que no vuelvan a llenar el form vacio
            messages.info(request,'Consulta enviada exitosamente🌸')
            return redirect(reverse('index'))

    else: #GET (necesito que el form este vacio - form "no vinculado")
        formulario= ContactoForm()
        #si yo necesitara poner un campo con un dato precargado se hace aca en plan
        #formulario= ContactoForm(
        # lugar_de_importacion= 'Argentina' (ah re siome, pero se entiende)
        # )

    context= {
        'contacto_form': formulario
    }

    return render(request, 'core/contacto.html', context)

'''
def listar_productos(request):
    return render(request, 'core/listado_productos.html')
'''

#CREATE----------------------------------------------------------------------------------------------------------------------------------
def alta_producto(request):
    context= {}

    if request.method == 'POST':
        alta_form = AltaProductoForm(request.POST)

        if alta_form.is_valid():
            nuevo_producto = Figura(
                denominacion= alta_form.cleaned_data['denominacion'],
                personaje= alta_form.cleaned_data['personaje'],
                coleccion= alta_form.cleaned_data['coleccion'],
                compañias= alta_form.cleaned_data['compañias'],
                precio= alta_form.cleaned_data['precio'],
                #fecha_salida= alta_form.cleaned_data['fecha_salida'],
                #imagen= alta_form.cleaned_data['imagen'],
            )
            nuevo_producto.save()
            messages.info(request, 'Producto dado de alta correctamente')
            return redirect(reverse('index'))

    else:
        alta_form = AltaProductoForm()

    context['alta_producto_form'] = AltaProductoForm

    return render(request, 'core/alta_producto.html', context)


def alta_personaje(request):
    context= {}
    alta_form = AltaPersonajeForm(request.POST)

    if alta_form.is_valid():
        nuevo_pj= Personaje(
            nombre= alta_form.cleaned_data['nombre'],
            anime= alta_form.cleaned_data['anime']
        )
        nuevo_pj.save()
        messages.info(request, 'Personaje registrado correctamente')
        return redirect(reverse('index'))
    
    else:
        alta_form= AltaPersonajeForm()
    
    context['alta_personaje_form'] = AltaPersonajeForm

    return render(request, 'core/alta_personaje.html', context)

    
def alta_empresa(request):
    context= {}
    alta_form = AltaEmpresaForm(request.POST)

    if alta_form.is_valid():
        nueva_empresa= Compañia(
            nombre= alta_form.cleaned_data['nombre'],
            ubicacion= alta_form.cleaned_data['ubicacion']
        )
        nueva_empresa.save()
        messages.info(request, 'Compañia registrada correctamente')
        return redirect(reverse('index'))
    
    else:
        alta_form= AltaEmpresaForm()
    
    context['alta_empresa_form'] = AltaEmpresaForm

    return render(request, 'core/alta_empresa.html', context)

#READ----------------------------------------------------------------------------------------------------------------------------------

def listar_productos(request):
    listado = Figura.objects.all().order_by('id')

    context= {
        'listado_productos': listado,
        'cant_productos': len(listado),
    }

    return render(request, 'core/listado_productos.html',context)


def listar_personajes(request):
    listado= Personaje.objects.all().order_by('id')

    context= {
        'listado_pjs': listado,
        'cant_personajes': len(listado),
    }

    return render(request, 'core/listado_personajes.html', context)


def listar_empresas(request):
    listado= Compañia.objects.all().order_by('id')

    context= {
        'listado_emp': listado,
        'cant_empresas': len(listado)
    }

    return render(request, 'core/listado_compañias.html', context)

#UPDATE------------------------------------------------------------------------------------------------------------------------------
