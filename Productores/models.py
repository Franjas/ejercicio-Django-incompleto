from re import T
from unicodedata import name
from django.db import models

# Create your models here.

class film_producers(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Fecha_nacimiento = models.DateField(null=True, blank=True)
    Fecha_muerte = models.DateField('Died', null=True, blank=True)
    def __str__(self):
        return '%s, %s' % (self.Apellido, self.Nombre)
    

class Genre(models.Model):
    name = models.CharField(max_length=64,
                            help_text='Nombre del género')
    def __str__(self):
        return self.name
    

class films(models.Model):
    Título = models.CharField(
        max_length=32)
    Género = models.ManyToManyField(Genre)
    País = models.CharField(
        max_length=50)
    Duración = models.CharField(
        max_length=9)
    director = models.ForeignKey(
        'film_producers',
        on_delete=models.SET_NULL, null=True)
    Fecha_lanzamiento = models.CharField(
        max_length=15)
    Elenco = models.CharField(
        max_length=200)
    Sinopsis = models.TextField(
        max_length=500, 
        help_text='Una breve descripción del contenido')
    
    def __str__(self):
        return self.Título