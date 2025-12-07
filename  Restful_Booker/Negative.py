import pytest
import requests
from constants import BASE_URL


def test_negative_response():
    invalid_data = {
        "firstname": "",

    }
    response = requests.post(f"{BASE_URL}/booking", json=invalid_data)
    print(f"Данные : {invalid_data}")
    print(f"Статус:{response.status_code}")
    print(f"Ответ: {response.text[:100]}")

    assert response.status_code in [400, 422, 500], \
        f"Ожидался 400 для невалидных данных, получен {response.status_code}"


def test_negative_full_response():
    invalid_data = {
        "firstname": 1112,
        "lastname": 4232,
        "totalprice": 2,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-03-11",
            "checkout": "2025-03-24"
        },
        "additionalneeds": "IPhone"
    }

    response = requests.post(f"{BASE_URL}/booking",json=invalid_data)
    print(f"Данные : {invalid_data}")
    print(f"Статус:{response.status_code}")
    print(f"Ответ: {response.text[:100]}")
    assert  response.status_code in [400,422,500], \
    f"Ожидался 400 для невалидных данных, получен {response.status_code}"

def test_put_response():
    invalid_data = {

    }



    response = requests.post(f"{BASE_URL}/BOOKING", json=invalid_data)

    print(f"Данные : {invalid_data}")
    print(f"Статус:{response.status_code}")
    print(f"Ответ: {response.text[:100]}")


