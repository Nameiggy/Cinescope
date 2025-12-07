import requests

# s = requests.Session()
# s.headers.update({'User-Agent': 'My Custom Bot'}) # Постоянный заголовок
# s.auth = ('user', 'password') # Постоянная аутентификация
#
# response = s.get('https://httpbin.org/headers')
# print(response.json())
#
# response2 = s.post('https://httpbin.org/post', json={"data": "test"})
# print(response2.json())

# import time
# url = "https://httpbin.org/get"
# num_requests = 10
#
# print("Запросы с использованием сессии:")
# start_time = time.time()
#
# session = requests.session()
# try:
#     for i in range(num_requests):
#         response = session.get(url)
#         response.raise_for_status()
# except Exception as e:
#     print(f"ошибка: {e}")
# finally:
#     session.close()
# end_time = time.time()
# print(f"Время выполнения с сессией: {end_time - start_time:.4f} секунд\n")
#
#
# print("Запросы БЕЗ использования сессии:")
# start_time = time.time()
# try:
#     for i in range(num_requests):
#
# from requests.auth import HTTPBasicAuth
#
# url = "https://httpbin.org/basic-auth/user/passwd"  # URL, требующий Basic Auth
#
# response = requests.get(url, auth=HTTPBasicAuth('user', 'passwd'))
#
# print(f"Status code: {response.status_code}")
# print(response.json())

                                # Bearer Token
# url = "https://httpbin.org/bearer"
# token = "my_secret_token"
# headers = {'Authorization' : f"Bearer {token}"}
#
# response = requests.get(url,headers=headers)
#
# print(f'Status code : {response.status_code}')
# print(response.json())


                               # API Key (ключ API)
# url = "https://httpbin.org/headers"
# api_key = "my_api_key"
# headers = {'X-API-KEY' : api_key}
#
# response = requests.get(url, headers=headers)
#
# print(f"Status code: {response.status_code}")
# print(response.json())
                               # Refresh Token

# REFRESH_TOKEN_URL = "https://example.com/api/token/refresh"
#
# refresh_token = "YOUR_REFRESH_TOKEN"
#
# def refresh_access_token(refresh_token):
#     """Обновляет access токен с помощью refresh токена."""
#     data = {"refresh_token": refresh_token}
#     response = requests.post(REFRESH_TOKEN_URL, json=data)
#
#     if response.status_code == 200:
#         new_access_token = response.json().get("access_token")
#         new_refresh_token = response.json().get("refresh_token")
#         return new_access_token, new_refresh_token
#     else:
#         print(f"Ошибка обновления токена: {response.status_code}")
#         return None, None
#
# # Получаем оба токена
# new_access_token, new_refresh_token = refresh_access_token(refresh_token)
#
# if new_access_token:
#     print(f"Новый access токен: {new_access_token}")
#     if new_refresh_token:
#         print(f"Новый refresh токен: {new_refresh_token}")
#
#     # Дальше суем в заголовок/куки - в зависимости от реализации
#     headers = {"Authorization": f"Bearer {new_access_token}"}
#     response = requests.get("https://example.com/api/protected", headers=headers)

                         # OAuth2 (Open Authorization)

# Готовим данные
# auth_url = 'https://api.example.com/oauth2/token'
# client_id = 'your_client_id'
# client_secret = 'your_client_secret'
#
# data = {
#     'grant_type': 'client_credentials',
#     'client_id': client_id,
#     'client_secret': client_secret
# }
#
# # Получаем токен
# token_response = requests.post(auth_url, data=data)
# access_token = token_response.json().get('access_token')
#
# # используем
# headers = {
#     'Authorization': f'Bearer {access_token}'
# }
#
# response = requests.get('https://api.example.com/secure-data', headers=headers)
#
# if response.status_code == 200:
#     print("Авторизация через OAuth2 успешна!")
#     print(response.json())


# def my_function(url):
#     response = requests.get(url)  # Step Into My Code здесь
#     if response.status_code == 200:
#         return response.text
#     else:
#         return "Error"
#
# url = "https://www.example.com"
# content = my_function(url)
# print(content)