# def add(a, b):
#     return a + b
#
#
# class TestMyFunctions:
#
#     def test_add_positive_numbers(self):
#         assert add(2, 3) == 5
#
#     def test_add_negative_numbers(self):
#         assert add(-1, -4) == -5
#
#     def test_add_positive_and_negative(self):
#         assert add(5, -2) == 3
#
#     def test_add_string(self):
#         assert add("test", "string") == "test string"

# import pytest
#
# @pytest.fixture
# def input_data():
#     return [1,2,3,4,5]
#
#
# def test_sum(input_data):
#     assert sum(input_data) == 15
#
# def test_len(input_data):
#     assert len(input_data) == 5
import requests

# response = requests.get('https://restful-booker.herokuapp.com/booking')
# data = response.json()
#
# print(f"Тело ответа: {data}")
# print(f"можно обратиться по ключу, например к первому элементу: {data[0]}")

# booking_id = 1
# response = requests.get(f'https://restful-booker.herokuapp.com/booking/{booking_id}')
#
# data = response.json()
#
# print(f"Тело ответа: {data}")

# """
# response = requests.get(f'https://restful-booker.herokuapp.com/booking?firstname=Sally')
# """
# response = requests.get(f'https://restful-booker.herokuapp.com/booking',
#                         params={"firstname":"Sally"})
# data = response.json()
#
# print(f"Тело ответа: {data}")

# headers = {
#     'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64;x64) AppleWebkit/537.30',
#     'Accept' : 'application/json'
# }
#
# response = requests.get(
#     'https://restful-booker.herokuapp.com/booking',
#     headers=headers
# )
# print(response)

                             # Обработка ошибок
# try:
#     response = requests.get('https://restful-booker.herokuapp.com/booking')
#     response.raise_for_status()
#
#     data = response.json()
#     print(f"Получены данные: {data}")
#
# except requests.exceptions.ConnectionError:
#     print("Не удалось подключиться к серверу")
#
# except requests.exceptions.Timeout:
#     print("Сервер не отвечает слишком долго")
#
# except requests.exceptions.HTTPError as http_err:
#     print(f"Произошла HTTP ошибка: {http_err}")
#
# except requests.exceptions.RequestException as e:
#     print(f"Произошла ошибка при выполнении запроса: {e}")

                                   # POST запросы





# URL = "https://restful-booker.herokuapp.com/booking"
#
# def test_response():
#     data = {
#         "firstname": "Jim",
#         "lastname": "Brown",
#         "totalprice": 111,
#         "depositpaid": True,
#         "bookingdates": {
#             "checkin": "2025-01-04",
#             "checkout": "2025-01-15"
#         },
#         "additionalneeds": "Breakfast"
#     }
#
#     response = requests.post(URL,json=data)
#     assert response.status_code == 200,f"Expected 200, got {response.status_code}"
#
#     response_data = response.json()
#     booking_id = response_data["bookingid"]
#     print(f"Created booking with ID: {booking_id}")
#
#     get_url = f"{URL}/{booking_id}"
#     get_response = requests.get(get_url)
#
#     get_data = get_response.json()
#
#
#
#     assert get_data["lastname"] == data["lastname"]
#     assert get_data["totalprice"] == data["totalprice"]
#     assert get_data["depositpaid"] == data["depositpaid"]
#     assert get_data["bookingdates"]["checkin"] == data["bookingdates"]["checkin"]
#     assert get_data["bookingdates"]["checkout"] == data["bookingdates"]["checkout"]
#
#     print("✅ Booking created and verified successfully!")


# import json
# def test_run():
#
#     urls = "https://httpbin.org/status/204"  # Пустой ответ
#
#     response = requests.get(urls)
#
#     print(response.status_code)
#     print(dict(response.headers))
#     print(response.text)
#     print(response.content)
#
#     try:
#         json_data = response.json()
#         print(f"JSON Data: {json_data}")
#     except json.decoder.JSONDecodeError as e:
#         print(f"❌ JSONDecodeError occurred: {e}")
#         print(f"Error message: {str(e)}")
#         print(f"Error type: {type(e).__name__}")
#     except Exception as e:
#         print(f"❌ Other error: {e}")
#         print(f"Error type: {type(e).__name__}")


# if __name__ == "__main__":
#    test_run()