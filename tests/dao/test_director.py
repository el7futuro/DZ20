from unittest.mock import MagicMock
import pytest
import os

from dao.director import DirectorDAO
from dao.model.director import Director


@pytest.fixture
def director_dao():
    director_dao = DirectorDAO(None)

    sheridan = Director(id=1, name='sheridan')
    tarantino = Director(id=2, name='tarantino')
    vineshtock = Director(id=1, name='vineshtock')

    director_dao.get_one = MagicMock(return_value=sheridan)
    director_dao.get_all = MagicMock(return_value=[sheridan, tarantino, vineshtock])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    return director_dao

