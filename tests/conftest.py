from unittest.mock import MagicMock

import pytest

from dao.model.director import Director
from dao.director import DirectorDAO
from dao.model.genre import Genre
from dao.genre import GenreDAO
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture
def director_dao():
    director_dao = DirectorDAO(None)

    test_director1 = Director(id=1, name="Vasya")
    test_director2 = Director(id=2, name="John")
    test_director3 = Director(id=3, name="Kate")

    director_dao.get_all = MagicMock(return_value=[test_director1, test_director2])
    director_dao.get_one = MagicMock(return_value=test_director1)
    director_dao.create = MagicMock(return_value=test_director3)
    director_dao.update = MagicMock()
    director_dao.partially_update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


@pytest.fixture
def genre_dao():
    genre_dao = GenreDAO(None)

    g1 = Genre(id=1, name="Комедия")
    g2 = Genre(id=2, name="Семейный")
    g3 = Genre(id=3, name="Фэнтези")

    genre_dao.get_all = MagicMock(return_value=[g1, g2])
    genre_dao.get_one = MagicMock(return_value=g1)
    genre_dao.create = MagicMock(return_value=g3)
    genre_dao.update = MagicMock()
    genre_dao.partially_update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


@pytest.fixture
def movie_dao():
    movie_dao = MovieDAO(None)

    m1 = Movie(id=1, title="Властелин колец", description="Тут должно быть описание", trailer="Ссылка на трейлер",
               year=2020, rating=9.5, genre_id=5, director_id=4)
    m2 = Movie(id=2, title="Хоббит", description="Тут должно быть описание", trailer="Ссылка на трейлер",
               year=2018, rating=8.4, genre_id=5, director_id=3)
    m3 = Movie(id=3, title="Гарри Поттер", description="Тут должно быть описание", trailer="Ссылка на трейлер",
               year=2014, rating=7.9, genre_id=2, director_id=1)

    movie_dao.get_all = MagicMock(return_value=[m1, m2])
    movie_dao.get_one = MagicMock(return_value=m1)
    movie_dao.create = MagicMock(return_value=m3)
    movie_dao.update = MagicMock()
    movie_dao.partially_update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao
