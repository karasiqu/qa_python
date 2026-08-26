import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # 1. Проверка, что книги с возрастным рейтингом отсутствуют в списке книг для детей
    def test_get_books_for_children_without_age_rating(self):
        collector = BooksCollector()

        collector.add_new_book('Алиса в стране чудес')
        collector.add_new_book('Кладбище домашних животных')
        collector.set_book_genre('Алиса в стране чудес', 'Мультфильмы')
        collector.set_book_genre('Кладбище домашних животных', 'Ужасы')

        assert collector.get_books_for_children() == ['Алиса в стране чудес']

    # 2. Проверка, что у добавленной книги нет жанра, если его не указывать при добавлении
    def test_add_new_book_without_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')

        assert collector.get_book_genre('Дюна') == ''

    # 3. Проверка, что добавленной книге можно установить жанр
    def test_set_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    # 4. Проверка, что книгу с одним и тем же названием нельзя добавить повторно
    def test_add_new_book_duplicate(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')

        assert len(collector.get_books_genre()) == 1

    # 5. Проверка, что можно получить список книг определенного жанра
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.add_new_book('Кладбище домашних животных')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Кладбище домашних животных', 'Ужасы')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна']

    # 6. Проверка, что книгу можно добавить в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')

        assert collector.get_list_of_favorites_books() == ['Дюна']

    # 7. Проверка, что одну и ту же книгу нельзя добавить в избранное повторно 
    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Дюна')

        assert collector.get_list_of_favorites_books() == ['Дюна']

    # 8. Проверка, что книгу можно удалить из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')

        assert collector.get_list_of_favorites_books() == []

    # 9. Проверка, что нельзя добавить книгу с пустым названием или названием больше 40 символов
    @pytest.mark.parametrize('name', ['', 'А' * 41])
    def test_add_new_book_invalid_name(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert name not in collector.get_books_genre()

    # 10. Проверка получения словаря с книгами и их жанрами
    def test_get_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        assert collector.get_books_genre() == {'Дюна': 'Фантастика'}

    # 11. Проверка получения жанра книги по ее названию
    def test_get_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        assert collector.get_book_genre('Дюна') == 'Фантастика'

    # 12. Проверка получения списка избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')

        assert collector.get_list_of_favorites_books() == ['Дюна']


    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()