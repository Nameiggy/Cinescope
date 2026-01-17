


import random
import string
from faker import Faker




class MovieDataGenerator:
    faker = Faker()  # Создаем один экземпляр Faker для всех методов

    @staticmethod
    def generate_movie_name() -> str:
        """Генерирует случайное название фильма."""
        # Варианты паттернов для названий
        patterns = [
            f"{MovieDataGenerator.faker.word().capitalize()} {MovieDataGenerator.faker.word()}",
            f"The {MovieDataGenerator.faker.word().capitalize()}",
            f"{MovieDataGenerator.faker.first_name()}'s {MovieDataGenerator.faker.word().capitalize()}",
            MovieDataGenerator.faker.catch_phrase()
        ]
        return random.choice(patterns)

    @staticmethod
    def generate_image_url() -> str:
        """Генерирует случайный URL картинки."""
        # Можно использовать разные сервисы
        services = [
            f"https://picsum.photos/400/300?random={random.randint(1, 1000)}",
            f"https://placekitten.com/{random.randint(300, 500)}/{random.randint(200, 400)}",
            f"https://dummyimage.com/{random.randint(300, 600)}x{random.randint(200, 400)}/000/fff"
        ]
        return random.choice(services)

    @staticmethod
    def generate_price() -> int:
        """Генерирует случайную цену."""
        return random.randint(100, 1000)

    @staticmethod
    def generate_description() -> str:
        """Генерирует описание фильма."""
        return MovieDataGenerator.faker.paragraph(nb_sentences=random.randint(2, 4))

    @staticmethod
    def generate_location() -> str:
        """Генерирует локацию."""
        return random.choice(['SPB', 'MSK'])

    @staticmethod
    def generate_genre_id() -> int:
        """Генерирует ID жанра."""
        return random.randint(1, 10)

    @staticmethod
    def generate_complete_movie_data() -> dict:
        """Генерирует полные данные для фильма."""
        return {
            "name": MovieDataGenerator.generate_movie_name(),
            "imageUrl": MovieDataGenerator.generate_image_url(),
            "price": MovieDataGenerator.generate_price(),
            "description": MovieDataGenerator.generate_description(),
            "location": MovieDataGenerator.generate_location(),
            "published":random.choice([True, False]),
            "genreId": MovieDataGenerator.generate_genre_id()
        }