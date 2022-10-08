from unittest.mock import MagicMock
import pytest
import os

from dao.genre import GenreDAO
from dao.model.genre import Genre


@pytest.fixture
def genre_dao():
    genre_dao = GenreDAO(None)

    comedy = Genre(id=1, name='Комедия')
    family = Genre(id=2, name='Семейный')
    fantasy = Genre(id=1, name='Фэнтези')

    genre_dao.get_one = MagicMock(return_value=comedy)
    genre_dao.get_all = MagicMock(return_value=[comedy, family, fantasy])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()
    return genre_dao
