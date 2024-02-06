import pytest
import requests
import random
import data.configuration as config
from src.generators.user import User


@pytest.fixture
def get_users_list():
    r = requests.get(url=config.SERVISE_URL + "users?page=2")
    return r

@pytest.fixture
def get_user_generator():
    return User()

@pytest.fixture
def calculate():
    return _calculate


def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None


@pytest.fixture
def make_number():
    number = random.randrange(1, 1000, 5)
    yield