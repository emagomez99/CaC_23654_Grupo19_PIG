from django.contrib import admin
from core.models import Figura, Personaje, Compañia, Administrador, Vendedor

class FiguraAdmin(admin.ModelAdmin):
    filter_horizontal = ('compañias',)

admin.site.register(Figura, FiguraAdmin)
admin.site.register(Personaje)
admin.site.register(Compañia)
admin.site.register(Administrador)
admin.site.register(Vendedor)