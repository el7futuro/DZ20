import pytest

from service.genre import GenreService
from tests.dao.test_genre import genre_dao

class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genre = self.genre_service.get_all()
        assert len(genre) > 0

    def test_create(self):
        genre_d ={
            "name": "horror",
        }

        genre = self.genre_service.create(genre_d)
        assert genre.id is not None

    def test_update(self):
        genre_d = {
            "id": 3,
            "name": "anime"
        }

        self.genre_service.update(genre_d)

    def delete(self):
        self.genre_service.delete(1)