from django.shortcuts import render, get_object_or_404
from django.db.models import F, Max, Min, Count, Avg, Value
from .models import Movie, Actor, Director
from django.views.generic import ListView, DetailView


def show_all_movie(request):
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        str_field=Value('hello'),
        int_field=Value(123),
        new_budget=F('budget') + 100,
        ffff=F('rating') * F('years'),
    ).order_by('name', F('years').desc(nulls_last=True))

    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))

    return render(request, 'movie_app/all_movies.html', context={
        'movies': movies,
        'agg': agg,
        'total_count': movies.count(),
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', context={
        'movie': movie}
    )


class ShowAllActors(ListView):
    model = Actor
    template_name = 'movie_app/all_actors.html'
    context_object_name = 'actors'


class ShowOneActor(DetailView):
    model = Actor
    template_name = 'movie_app/one_actor.html'


class ShowAllDirectors(ListView):
    model = Director
    template_name = 'movie_app/all_directors.html'
    context_object_name = 'directors'


class ShowOneDirector(DetailView):
    model = Director
    template_name = 'movie_app/one_director.html'
