from typing import List
from django.db.models import QuerySet

from db.models import Movie


def get_movie_by_id(
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> QuerySet:

    movies = Movie.objects.all()

    if genres_ids:
        return Movie.objects.filter(genre_id__in=genres_ids)
    if actors_ids:
        return Movie.objects.filter(actor_id__in=actors_ids)

    return movies.distinct()


def get_movies_by_id(movie_id: int) -> QuerySet:
    movies = Movie.objects.filter(id=movie_id)
    return movies


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> Movie:

    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        movie.genres.set(genres_ids)

    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
