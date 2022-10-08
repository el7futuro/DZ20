from unittest.mock import MagicMock
import pytest
import os

from dao.movie import MovieDAO
from dao.model.movie import Movie


@pytest.fixture
def movie_dao():
    movie_dao = MovieDAO(None)

    yellowstone = Movie(id=1,
                        title='Йеллоустоун',
                        description='Владелец ранчо пытается сохранить землю своих предков. ',
                        trailer='https://www.youtube.com/watch?v=UKei_d0cbP4',
                        year='2018',
                        rating='8.6',
                        genre_id='17',
                        director_id='1')
    eight_ = Movie(id=2,
                   title='Омерзительная восьмерка',
                   description='США после Гражданской войны.',
                   trailer='https://www.youtube.com/watch?v=lmB9VWm0okU',
                   year='2015',
                   rating='7.8',
                   genre_id='4',
                   director_id='2'
                   )
    armed_ = Movie(id=3,
                   title='Вооружен и очень опасен',
                   description='События происходят в конце XIX века на Диком Западе',
                   trailer='https://www.youtube.com/watch?v=hLA5631F-jo',
                   year='1978',
                   rating='6',
                   genre_id='17',
                   director_id='3')

    movie_dao.get_one = MagicMock(return_value=yellowstone)
    movie_dao.get_all = MagicMock(return_value=[yellowstone, eight_, armed_])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao
