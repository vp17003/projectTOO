from django.urls import path
from registroAsociado.views import * 

urlpatterns = [
	path('ejecutivo', ListEjecutivo, name="verEjecutivo"),
	path('ejecutivoAgregar', crearEjecutivo, name="registrarEjecutivo"),	
	path('modificar/<int:ejecutivoID>', UpdateEjecutivo, name="updateEjecutivo"),
	# path('transaccion/agregar', CreateTransaccion, name="registrarTransaccion"),	

    
]

