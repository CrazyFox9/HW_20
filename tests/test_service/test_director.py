import os
from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture
def director_dao():
    director_dao = DirectorDAO(None)

    test_director1 = Director(id=1, name="Vasya")
    test_director2 = Director(id=2, name="John")
    test_director3 = Director(id=3, name="Kate")

    director_dao.get_all = MagicMock(return_value=[test_director1, test_director2, test_director3])
    director_dao.get_one = MagicMock(return_value=test_director1)
    director_dao.create = MagicMock()
    director_dao.update = MagicMock()
    director_dao.partially_update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None

    def test_create(self):
        director_d = {
            "name": "Test"
        }

        director = self.director_service.create(director_d)
        assert director.id is not None

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        director_d = {
            "id": 2,
            "name": "Test",
        }

        self.director_service.update(director_d)

    def test_partially_update(self):
        director_d = {
            "id": 2,
            "name": "Test",
        }
        self.director_service.partially_update(director_d)


if __name__ == "__main__":
    os.system("pytest")
