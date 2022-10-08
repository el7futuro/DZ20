import pytest

from service.director import DirectorService
from tests.dao.test_director import director_dao

class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        director = self.director_service.get_all()
        assert len(director) > 0

    def test_create(self):
        director_d ={
            "name": "allen",
        }

        director = self.director_service.create(director_d)
        assert director.id is not None

    def test_update(self):
        director_d = {
            "id": 3,
            "name": "uchitel"
        }

        self.director_service.update(director_d)

    def delete(self):
        self.director_service.delete(1)