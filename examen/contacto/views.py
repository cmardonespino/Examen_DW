# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.http.response import HttpResponseRedirect

from django.shortcuts import render, HttpResponse, get_object_or_404

from principal.models import Contacto

def lista_contactos(request):
	data = {}
	data['datos'] = Contacto.objects.all()
	template_name = 'contacto.html'
	return render(request, template_name, data)

def detalle_contacto(request, pk):
	contacto = get_object_or_404(Contacto, pk=pk)
	template_name = 'detalle.html'
	return render(request, template_name, {'detalle_contacto': contacto})