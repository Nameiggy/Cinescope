import json
import pytest
import requests


from Movies.constans import  Admin_URL, LOGIN_ENDPOINT, SUPER_ADMIN
from Movies.custrim_request.CostomRequest import CustomRequester
from Movies.test.API.API_Manegment import ApiManager
from Movies.utils.Movie_data_generator import MovieDataGenerator


@pytest.fixture(scope="session")
def info_movies(api_manager):
    response = api_manager.api_get_movies.get_movies()

    if response.status_code == 200:
        data = response.json()
        movies = data.get('movies', [])

        print(f"\n" + "=" * 50)
        print(f"ВСЕГО ФИЛЬМОВ НА СТРАНИЦЕ: {len(movies)}")
        print("=" * 50)

        for movie in movies:
            print("\n" + "=" * 50)
            print(f"ФИЛЬМ ID: {movie.get('id')}")
            print("=" * 50)

            # JSON с отступами
            movie_json = json.dumps(movie, ensure_ascii=False, indent=2)
            print(movie_json)

        return data  # полный ответ
    return []


@pytest.fixture
def filtered_movies(api_manager):
    """Фикстура для тестирования фильтров"""
    response = api_manager.api_get_movies.get_movies(params={"genreId": 1})

    data = response.json()

    # Обрабатываем структуру ответа
    if isinstance(data, dict) and "movies" in data:
        movies = data["movies"]
    elif isinstance(data, list):
        movies = data
    else:
        pytest.fail(f"Неизвестный формат ответа: {type(data)}")
        return []  # на случай если pytest.fail не остановит выполнение

    return movies





@pytest.fixture(scope="session")
def post_movies_session(api_manager,movie_test_data,admin_auth_session):

    response = api_manager.api_post_movies.post_movies(movie_test_data)

    if response.status_code == 201:
        movie = response.json()


        formatted_movie = {
            "id": movie.get('id'),
            "name": movie.get('name'),
            "price": movie.get('price'),
            "description": movie.get('description'),
            "imageUrl": movie.get('imageUrl'),
            "location": movie.get('location'),
            "published": movie.get('published'),
            "genreId": movie.get('genreId'),
            "genre": {
                "name": movie.get('genre', {}).get('name', '')
            },
            "createdAt": movie.get('createdAt'),
            "rating": movie.get('rating', 0)
        }


        print("\n" + "=" * 50)
        print(" СОЗДАННЫЙ ФИЛЬМ:")
        print("=" * 50)
        print(json.dumps(formatted_movie, indent=2, ensure_ascii=False))
        print("=" * 50)

        print(f" Фильм создан: {formatted_movie['name']} (ID: {formatted_movie['id']})")

        return formatted_movie
    else:
        pytest.fail(f" Не удалось создать фильм. Статус: {response.status_code}, Ответ: {response.text}")
        return None



@pytest.fixture(scope="session")
def patch_movies(api_manager,movie_patch_data,admin_auth_session):

    response = api_manager.api_patch_movies.patch_movie(movie_patch_data)

    if response.status_code == 200:
        movie = response.json()

        formatted_movie = {
            "id": movie.get('id'),
            "name": movie.get('name'),
            "price": movie.get('price'),
            "description": movie.get('description'),
            "imageUrl": movie.get('imageUrl'),
            "location": movie.get('location'),
            "published": movie.get('published'),
            "genreId": movie.get('genreId'),
            "genre": {
                "name": movie.get('genre', {}).get('name', '')
            },
            "createdAt": movie.get('createdAt'),
            "rating": movie.get('rating', 0)
        }

        print("\n" + "=" * 50)
        print(" ОБНОВЛЕННЫЙ ФИЛЬМ:")
        print("=" * 50)
        print(json.dumps(formatted_movie, indent=2, ensure_ascii=False))
        print("=" * 50)

        print("ОБНОВЛЕННЫЕ ПОЛЯ:")
        print("-" * 30)
        for key in ["name","description","price","location","imageUrl","published","genreId"]:
            if key in movie_patch_data:
                print(f"{key}:{movie_patch_data[key]}")
        print("-" * 30)

        return formatted_movie
    else:
        pytest.fail(f" Не удалось обновить фильм. Статус: {response.status_code}, Ответ: {response.text}")
        return None





@pytest.fixture(scope="session")
def movie_patch_data():

    return {
        "name": MovieDataGenerator.generate_movie_name(),
        "description": MovieDataGenerator.generate_description(),
        "price": MovieDataGenerator.generate_price(),
        "location": MovieDataGenerator.generate_location(),
        "imageUrl": MovieDataGenerator.generate_image_url(),
        "published": True,
        "genreId": MovieDataGenerator.generate_genre_id()
    }


@pytest.fixture(scope="session")
def movie_test_data():
    """Возвращает тестовые данные для фильма (без создания в БД)."""
    return {
        "name": MovieDataGenerator.generate_movie_name(),
        "imageUrl": MovieDataGenerator.generate_image_url(),
        "price": MovieDataGenerator.generate_price(),
        "description": MovieDataGenerator.generate_description(),
        "published": True,
        "location": MovieDataGenerator.generate_location(),
        "genreId": MovieDataGenerator.generate_genre_id()
    }


@pytest.fixture(scope="session")
def deletes_movies(api_manager,admin_auth_session,info_movies):
    movie_id = 249

    movie_name = "Unknown"
    for movie in info_movies.get("movies",[]):
        if movie.get("id") == movie_id:
            movie_name = movie.get("name","Unknown")
            break
    print(f"Удаляю: {movie_name} (ID: {movie_id})")

    try:
        response = api_manager.api_delete_movies.delete_movies(movie_id)

        if response.status_code == 200:
            print(f"Фильм удален {movie_name} (ID: {movie_id})")
            return True

    except ValueError as e:
        if "404" in str(e):
            print(f"Фильм с ID {movie_id} не найден")
            return True
        else:
            print(f"Ошибка при удалении фильма: {e}")



@pytest.fixture(scope="session")
def admin_auth_session(requester, session,api_manager):
    """Отдельная сессия для админа"""
    response = requester.send_request(
        method="POST",
        endpoint=LOGIN_ENDPOINT,
        data=SUPER_ADMIN,
        expected_status=200
    )
    if response.status_code == 200 or response.status_code == 201:
        token = response.json().get("token") or response.json().get("accessToken")

        api_manager.session.headers.update({
            "Authorization": f"Bearer {token}"
        })

        return api_manager.session
    return None


@pytest.fixture(scope="session")
def requester():
    session = requests.session()
    return CustomRequester(session=session,base_url=Admin_URL)


@pytest.fixture(scope="session")
def api_manager(session):
    """
    Фикстура для создания экземпляра ApiManager.
    """
    return ApiManager(session)


@pytest.fixture(scope="session")
def session():
    """
    Фикстура для создания HTTP-сессии.
    """
    http_session = requests.Session()
    yield http_session
    http_session.close()
