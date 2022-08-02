from django.shortcuts import render
from .models import film_producers, Genre, films


def index(request):
    num_productores = film_producers.objects.all().count()
    num_generos = Genre.objects.all().count()
    num_películas = films.objects.all().count()
    
    return render(
        request,
        'index.html',
        context={
            'num_productores': num_productores,
            'num_generos': num_generos,
            'num_películas': num_películas
        }
    )