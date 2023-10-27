from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index (request):
    return render(request, "turnos/index.html", {"hoy":datetime.now})    

def servicios (request):

    data = [
        {"id": 1, "nombre": "Futbol 5", "duracion": "60 minutos", "activo": True},
        {"id": 2, "nombre": "Futbol 11", "duracion": "105 minutos", "activo": True},
        {"id": 3, "nombre": "Futbol infantil", "duracion": "45 minutos", "activo": True},
    ]
    return HttpResponse(data)
