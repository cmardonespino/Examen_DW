# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Contacto

class ContactosUsuarios(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'apellido', 'Email', 'Telefono', 'Direccion', 'imagen')
	list_filter = ('id'),
	list_search = ('nombre','apellido')

admin.site.register(Contacto,ContactosUsuarios)