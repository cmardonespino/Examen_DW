# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.

class Contacto(models.Model):
       nombre = models.CharField(max_length=200)
       apellido = models.CharField(max_length=200)
       Email= models.CharField(max_length=200)
       Telefono = models.CharField(max_length=200)
       Direccion = models.CharField(max_length=200)
       imagen = models.ImageField(upload_to='img')

       def __str__(self):
              return (self.nombre)