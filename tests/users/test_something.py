import pytest
import requests

import data.configuration as config

from src.baseclasses.response import Response
from src.schemas.get_user_list import USER_LIST_SCHEMA
from src.pydantic_schemas.get_user_list import UserList


def test_equal():
    assert 1 == 1, "Number not equal to expected"


def test_is_not_equal():
    assert 1 != 2, "Number is equal "


def test_status_code_getting_user_list(get_users_list):
    # r = requests.get(url=config.SERVISE_URL+"users?page=2")

    response = Response(get_users_list)
    response.assert_status_code(200).validate(UserList)

    # received_posts = response.json()
    #
    # assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    # assert len(received_posts) == 6, GlobalErrorMessages.WRONG_ELEMENT_COUNT

    # print(response.json())


def test_calculate_something(calculate):
    print(calculate)
    print(calculate(1, 1))


@pytest.mark.skip('[ISSUE-23141] Issue with network connection')
def test_first():
    print("first")


def test_calculation_both_negative(calculate):
    print(calculate(-1, -2))


def test_calculation_one_negative(calculate):
    print(calculate(-1, 2))


def test_calculation_both_positive(calculate):
    print(calculate(1, 2))


def test_calculation_one_char(calculate):
    print(calculate('a', 2))


def test_calculation_two_char(calculate):
    print(calculate('b', 'a'))

@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ('a', 2, None),
    ('a', 'b', None)
])
def test_calculator(first_value, second_value, result, calculate):
    """
        In that test we are try to check that calculator is work
        In that test we are try to check that calculator is work
    """
    assert calculate(first_value, second_value) == result

@pytest.mark.parametrize('status', [
    'ACTIVE',
    'BANNED',
    'DELETED',
    'INACTIVE'
])
def test_generator(status, get_user_generator):
    print(get_user_generator.set_status(status).build())