from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from registroAsociado.forms import *
from django.views.generic import ListView, CreateView
from datetime import datetime

def crearEjecutivo(request):	
	if request.method == 'GET':
		form = EjecutivoForm()
	else:
		form = EjecutivoForm(request.POST)
		if form.is_valid():			
			form.save()
		return redirect('registrarEjecutivo')
	return render(request, 'ejecutivos/registrarEjecutivo.html', {'form':form})


def ListEjecutivo(request):
	if request.method =='GET':
		ejecutivos= ejecutivo.objects.all().order_by('-idEjecutivo')	
		contexto={'ejecutivos':ejecutivos}
	else:
		return redirect('verEjecutivo')
	return render(request, 'ejecutivos/verEjecutivo.html', contexto)
	

def UpdateEjecutivo(request, ejecutivoID):
	ejecutivos = ejecutivo.objects.get(idEjecutivo = ejecutivoID)
	if request.method == 'GET':
		form = EjecutivoForm(instance=ejecutivos)
	else:
		form = EjecutivoForm(request.POST, instance=ejecutivos)
		if form.is_valid():
			form.save()			
		return redirect('verEjecutivo')
	return render(request, 'ejecutivos/registrarEjecutivo.html', {'form':form})