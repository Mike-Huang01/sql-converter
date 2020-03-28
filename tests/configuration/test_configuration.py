import pytest
from settings.settings import get_config


@pytest.fixture()
def config():
    return get_config("config.sample.yaml")


def test_file_absolute_path(config):
    path = config.get_file_path()
    assert "settings/files/config.sample.yaml" in path


def test_get_file_content(config):
    content = config.get_file_content()
    expected = {'db':
        {
            'host': 'localhost',
            'port': 0,
            'user': 'root',
            'name': 'mysql database name',
            'password': 'psswd'
        }
    }
    assert content == expected


def test_get_item(config):
    id = config.get["db"]['host']
    assert id == "localhost"


def test_get_wrong_item(config):
    with pytest.raises(KeyError):
        whatever = config.get["whatever"]


def test_should_print_repr_for_config(config):
    assert repr(config) == "<Configuration: config.sample.yaml>"
