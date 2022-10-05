import pytest

from service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None
        assert genre.name == "Комедия"

    def test_create(self):
        genre_d = {"name": "Фэнтези"}
        genre = self.genre_service.create(genre_d)
        assert genre.id is not None
        assert genre.name == "Фэнтези"

    def test_delete(self):
        self.genre_service.delete(1)

    def test_update(self):
        genre_d = {
            "id": 2,
            "name": "Роман"
        }

        self.genre_service.update(genre_d)

    def test_partially_update(self):
        genre_d = {
            "id": 2,
            "name": "Роман"
        }
        self.genre_service.partially_update(genre_d)
