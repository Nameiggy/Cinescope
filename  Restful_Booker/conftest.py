import pytest
import requests
from faker import Faker
from constants import BASE_URL,HEADERS


faker = Faker()

@pytest.fixture(scope="session")
def auth_session():
    session = requests.session()
    session.headers.update(HEADERS)

    response = session.post(
        f"{BASE_URL}/auth",
        json={"username":"admin","password":"password123"}
    )
    assert response.status_code == 200
    token = response.json().get("token")
    assert token is not None

    session.headers.update({"Cookie":f"token = {token}"})
    return session


@pytest.fixture
def booking_data():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100 , max=10000000),
        "depositpaid": True,
        "bookingdates":{
            "checkin": "2025-04-05",
            "checkout": "2025-04-10"
        },
        "additionalneeds": "Cigars"

    }

@pytest.fixture
def new_booking():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=10000000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-03-11",
            "checkout": "2025-03-24"
        },
        "additionalneeds": "IPhone"

    }