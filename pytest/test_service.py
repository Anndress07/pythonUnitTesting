import pytest
import requests

import source.service as service
import unittest.mock as mock

@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = service.get_user_from_db(2)

    assert user_name == "Mocked Alice"


@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id" : 1, "name" : "John Doe"}
    mock_get.return_value = mock_response
    """ when previous line gets called, it goes to access API on source/service.py, but we are mocking it
        so instead of going to the API it goes to line 16, 17 of this function. 
    """

    data = service.get_users()

    assert data == {"id" : 1, "name" : "John Doe"}

@mock.patch("requests.get")
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_get.return_value = mock_response
    # WE ARE EXPECTING A FAIL WITH THIS TEST
    with pytest.raises(requests.HTTPError):
        service.get_users()
