from django import forms
from registroAsociado.models import *
from django.contrib.admin.widgets import AdminDateWidget

errores = {
    'required': 'Este campo es obligatorio',
    'invalid': 'El dato ingresado no es valido'
}

class EjecutivoForm(forms.ModelForm):
	class Meta:
		model = ejecutivo
		fields =[
        'nombreEjecutivo',
        'apellidoEjecutivo'
		]

		labels = {
        'nombreEjecutivo': 'Nombres',
        'apellidoEjecutivo':'Apellidos'
		}

		widgets= {
        'nombreEjecutivo': forms.TextInput(attrs={'class':'form-control'}),
        'apellidoEjecutivo': forms.TextInput(attrs={'class':'form-control'})
		}
