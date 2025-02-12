from django.shortcuts import render, get_object_or_404
from django.db.models import F, Max, Min, Count, Avg, Value
from .models import Movie, Actor, Director


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


def show_all_actors(request):
    actors = Actor.objects.all()
    return render(request, 'movie_app/all_actors.html', context={'actors': actors})


def show_one_actor(request, id_actor):
    actor = get_object_or_404(Actor, id=id_actor)
    return render(request, 'movie_app/one_actor.html', context={'actor': actor})


def show_all_directors(request):
    directors = Director.objects.all()
    return render(request, 'movie_app/all_directors.html', context={'directors': directors})


def show_one_director(request, id_director):
    director = get_object_or_404(Director, id=id_director)
    return render(request, 'movie_app/one_director.html', context={'director': director})
