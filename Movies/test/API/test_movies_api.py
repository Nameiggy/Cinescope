
import json


from Movies.conftest import info_movies
from Movies.test.API.API_Manegment  import ApiManager



class TestApi:
    def test_get_movies (self,api_manager:ApiManager, info_movies):

        movies = info_movies.get('movies', [])
        assert len(movies) > 0, "Должен быть хотя бы один фильм"


    def test_genre_filter_works(self,filtered_movies):
        # Проверяем фильтрацию
        for movie in filtered_movies:
                assert movie["genreId"] == 1
        print(f"✓ Фильтрация работает: {len(filtered_movies)} фильмов с genreId=1")


    def test_post_movies(self,api_manager: ApiManager,post_movies_session):
        assert post_movies_session is not None,"Фикстура не вернула данные о созданном фильме"

        created_movie = post_movies_session

        # Проверяем обязательные поля в ответе
        assert "id" in created_movie, "Отсутствует поле 'id' в ответе"
        assert "name" in created_movie, "Отсутствует поле 'name' в ответе"
        assert "price" in created_movie, "Отсутствует поле 'price' в ответе"
        assert "description" in created_movie, "Отсутствует поле 'description' в ответе"
        assert "genreId" in created_movie, "Отсутствует поле 'genreId' в ответе"



    def test_movies_id(self,api_manager:ApiManager):

        movies = api_manager.api_get_movies.get_movies()

        data = movies.json()
        if isinstance(data,dict) and "movies" in data:
            movies = data["movies"]
        else:
            movies = []

        target_movie = None
        for movie in movies:
            if movie.get("id") == 215:
                target_movie = json.dumps(movie, ensure_ascii=False, indent=2)
                print(target_movie)
                break
        assert target_movie is not None,f"Фильм с ID  не найден"
        assert "id" in target_movie
        assert "name" in target_movie
        assert "price" in target_movie
        assert "description" in target_movie
        assert "genreId" in target_movie


    def test_delete_movie(self,api_manager: ApiManager, deletes_movies):

        assert deletes_movies is True, " Фильм не был удален"
        print(f" Фильм успешно удален")


    def test_patch_movies(self,api_manager: ApiManager,patch_movies):

        assert patch_movies is not None
        assert "name" in patch_movies,"Отсутствует поле 'name' в ответе"
        assert "description" in patch_movies,"Отсутствует поле 'description' в ответе"
        assert "price" in patch_movies,"Отсутствует поле 'price' в ответе"
        assert "location" in patch_movies,"Отсутствует поле 'location' в ответе"
        assert "imageUrl" in patch_movies,"Отсутствует поле 'imageUrl' в ответе"
        assert "published" in patch_movies,"Отсутствует поле 'published' в ответе"
        assert "genreId" in patch_movies,"Отсутствует поле 'genreId' в ответе"