import pytest

from service.movie import MovieService
from tests.dao.test_movie import movie_dao

class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movie = self.movie_service.get_all()
        assert len(movie) > 0

    def test_create(self):
        movie_d = {
                  "id": 1,
                  "title": "Йеллоустоун",
                  "description": "Владелец ранчо пытается сохранить землю своих предков.",
                  "trailer": "https://www.youtube.com/watch?v=UKei_d0cbP4",
                  "year": "2018",
                  "rating": "8.6",
                  "genre_id": "17",
                  "director_id": "1"
        }

        movie = self.movie_service.create(movie_d)
        assert movie.id is not None

    def test_update(self):
        movie_d = {
            "id": 1,
                  "title": "Йеллоустоун",
                  "description": "Владелец ранчо пытается сохранить землю своих предков.",
                  "trailer": "https://www.youtube.com/watch?v=UKei_d0cbP4",
                  "year": "2018",
                  "rating": "7.6",
                  "genre_id": "17",
                  "director_id": "1"
        }

        self.movie_service.update(movie_d)

    def delete(self):
        self.movie_service.delete(1)