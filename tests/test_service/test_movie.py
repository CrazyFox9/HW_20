import pytest

from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None
        assert movie.title == "Властелин колец"

    def test_create(self):
        movie_d = {
            "title": "Гарри Поттер",
            "description": "Тут должно быть описание",
            "trailer": "Ссылка на трейлер",
            "year": 2014,
            "rating": 7.9,
            "genre_id": 2,
            "director_id": 1
        }
        movie = self.movie_service.create(movie_d)
        assert movie.id is not None
        assert movie.title == "Гарри Поттер"
        assert movie.description == "Тут должно быть описание"
        assert movie.trailer == "Ссылка на трейлер"
        assert movie.year == 2014
        assert movie.rating == 7.9
        assert movie.genre_id == 2
        assert movie.director_id == 1

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            "title": "Test",
            "description": "Test",
            "trailer": "Test",
            "year": 2014,
            "rating": 7.9,
            "genre_id": 2,
            "director_id": 1
        }

        self.movie_service.update(movie_d)

    def test_partially_update(self):
        movie_d = {
            "id": 1,
            "title": "Test",
            "description": "Test",
            "trailer": "Test"
        }
        self.movie_service.partially_update(movie_d)
