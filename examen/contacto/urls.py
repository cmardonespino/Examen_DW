from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^contacto', views.lista_contactos, name="contacto"),
	#url(r'^detalle/(?P<pk>[0-9]+)/$', views.detalle_contacto, name='detalle'),
]