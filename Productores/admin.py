from django.contrib import admin

from .models import film_producers, Genre, films

admin.site.register(film_producers)
admin.site.register(Genre)
admin.site.register(films)
