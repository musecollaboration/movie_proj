from django.test import TestCase
from django.urls import reverse
from .models import Movie


class MovieModelTestCase(TestCase):

    @staticmethod
    def print_info(message):
        count = Movie.objects.count()
        print(f"{message}: #all_movies={count}")

    def setUp(self):
        print('-' * 20)
        self.print_info('Start setUp')
        self.movie = Movie.objects.create(name='Test Movie', rating=80, years=2022)
        Movie.objects.create(name='Test Matrix', rating=90, years=2021)
        Movie.objects.create(name='Mask', rating=50, years=1995)
        self.print_info('Finish setUp')

    def test_movie_creation(self):
        # Проверка создания объекта Movie
        self.print_info('Start test_movie_creation')
        self.assertEqual(self.movie.name, 'Test Movie')
        self.assertEqual(self.movie.rating, 80)
        self.assertEqual(self.movie.years, 2022)
        self.assertEqual(self.movie.budget, 1000000)
        self.assertEqual(self.movie.slug, 'test-movie')
        self.print_info('Finish test_movie_creation')

    def test_movie_get_all_records(self):
        # Проверка получения всех записей из бд
        self.print_info('Start test_movie_get_all_records')
        movies = Movie.objects.all()
        self.assertEqual(len(movies), 3)
        self.print_info('Finish test_movie_get_all_records')

    def test_movie_get_record(self):
        # Проверка получения записи из бд
        self.print_info('Start test_movie_get_record')
        mask = Movie.objects.get(name='Mask')
        self.assertEqual(mask.years, 1995)
        self.print_info('Finish test_movie_get_record')

    def test_movie_get_url(self):
        # Проверка метода get_url()
        self.print_info('Start test_movie_get_url')
        url = self.movie.get_url()
        expected_url = reverse('url_name', args=['test-movie'])
        self.assertEqual(url, expected_url)
        self.print_info('Finish test_movie_get_url')

    def test_movie_str(self):
        # Проверка метода __str__()
        self.print_info('Start test_movie_str')
        expected_str = 'Test Movie - 80%'
        self.assertEqual(str(self.movie), expected_str)
        self.print_info('Finish test_movie_str')

    def test_movie_save_slug(self):
        # Проверка сохранения корректного slug при сохранении объекта
        self.print_info('Start test_movie_creation')
        self.assertEqual(self.movie.slug, 'test-movie')
        self.print_info('Finish test_movie_save_slug')

    def test_movie_budget_default_value(self):
        # Проверка значения по умолчанию для budget
        self.print_info('Start test_movie_budget_default_value')
        movie = Movie.objects.create(name='Default Budget Movie', rating=75)
        self.assertEqual(movie.budget, 1000000)
        self.print_info('Finish test_movie_budget_default_value')

    def test_movie_deletion(self):
        # Проверка удаления записи
        self.print_info('Start test_movie_deletion')
        initial_count = Movie.objects.count()
        self.movie.delete()
        new_count = Movie.objects.count()
        self.assertEqual(new_count, initial_count - 1)
        self.print_info('Finish test_movie_deletion')

    def test_movie_update(self):
        # Проверка изменений данных в записи
        self.print_info('Start test_movie_update')
        self.movie.name = 'Updated Movie'
        self.movie.rating = 85
        self.movie.years = 2023
        self.movie.save()

        updated_movie = Movie.objects.get(id=self.movie.id)
        self.assertEqual(updated_movie.name, 'Updated Movie')
        self.assertEqual(updated_movie.rating, 85)
        self.assertEqual(updated_movie.years, 2023)
        self.print_info('Finish test_movie_update')
