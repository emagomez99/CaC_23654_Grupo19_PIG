from django import forms

class EspacioForm(forms.Form):
    id= forms.IntegerField(label="ID", required= True) #este capas no porque va a ser autoincremental pero bueno.
    nombre= forms.CharField(label= "Nombre", required= True)
    detalle= forms.CharField(label= "Detalle", widget=forms.Textarea)
    habilitado= forms.BooleanField(label= "Lugar habilitado", required= True)

