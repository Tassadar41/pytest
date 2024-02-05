import requests

import data.configuration as config

from src.baseclasses.response import Response
from src.schemas.get_user_list import USER_LIST_SCHEMA
from src.pydantic_schemas.get_user_list import UserList


def test_equal():
    assert 1 == 1, "Number not equal to expected"

def test_is_not_equal():
    assert 1 != 2, "Number is equal "

def test_status_code_getting_user_list():
    r = requests.get(url=config.SERVISE_URL+"users?page=2")
    response = Response(r)

    response.assert_status_code(200).validate(UserList)

    # received_posts = response.json()
    #
    # assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    # assert len(received_posts) == 6, GlobalErrorMessages.WRONG_ELEMENT_COUNT

    ##print(response.json())
