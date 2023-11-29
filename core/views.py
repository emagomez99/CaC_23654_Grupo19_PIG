from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactoForm, AltaProductoForm, AltaPersonajeForm, AltaEmpresaForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Figura, Personaje, Compañia
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

# TEMPLATE ASOCIADO A UNA VISTA---------------------------------------
def index(request):
    return render(request, 'core/index.html')

def contacto(request):
    if request.method == "POST":
        formulario= ContactoForm(request.POST)
        
        if formulario.is_valid(): 
            messages.info(request,'Consulta enviada exitosamente🌸')
            return redirect(reverse('index'))

    else:
        formulario= ContactoForm()

    context= {
        'contacto_form': formulario
    }

    return render(request, 'core/contacto.html', context)

# FORMULARIO USADO EN VISTA BASADA EN CLASES ------------------------------------------------------------------
class AltaProductoView(CreateView):
    model = Figura
    form_class = AltaProductoForm
    template_name = 'core/alta_producto.html'

    def form_valid(self, form):
        messages.info(self.request, 'Producto dado de alta correctamente')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['alta_producto_form'] = self.form_class()
        return context

@permission_required('core.add_personaje', login_url='/login/', raise_exception=True)
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

@permission_required('core.add_personaje', login_url='/login/', raise_exception=True)
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
#VISTA PARAMETRIZADA ------------------------------------------------------------------------------------------------------------------

@login_required
def listar_productos(request):
    listado = Figura.objects.all().order_by('id')

    context= {
        'listado_productos': listado,
        'cant_productos': len(listado),
    }

    return render(request, 'core/listado_productos.html',context)

@login_required
def listar_personajes(request):
    listado= Personaje.objects.all().order_by('id')

    context= {
        'listado_pjs': listado,
        'cant_personajes': len(listado),
    }

    return render(request, 'core/listado_personajes.html', context)

@login_required
def listar_empresas(request):
    listado= Compañia.objects.all().order_by('id')

    context= {
        'listado_emp': listado,
        'cant_empresas': len(listado)
    }

    return render(request, 'core/listado_compañias.html', context)

#UPDATE------------------------------------------------------------------------------------------------------------------------------ clase 23 models 3 - antes de 0:53
#DELETE------------------------------------------------------------------------------------------------------------------------------