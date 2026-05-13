import pytest

from main import BooksCollector  

class TestBooksCollector:

    @pytest.mark.parametrize("book_name",["Валидное название", "o","е"*40])
    def test_add_new_books_valid_names (self,b_collector,book_name):
        b_collector.add_new_book(book_name)
        #проверяем что созданная книга есть в словаре
        assert book_name in b_collector.books_genre
        #проверяем что жанр пока пустой
        assert b_collector.books_genre[book_name]==''

    #проверяем негативные варианты названий книг
    @pytest.mark.parametrize("book_name",["","е"*41])
    def test_add_new_books_not_valid_names (self,b_collector,book_name):
        b_collector.add_new_book(book_name)
        #проверяем что книга не добавлена в словарь
        assert book_name not in b_collector.books_genre

    #проверяем повторное добавление названия книги
    def test_add_new_books_duplicate(self, b_collector):
        book_name='Солярис'
        b_collector.add_new_book(book_name)
        b_collector.add_new_book(book_name) 
        assert len(b_collector.books_genre) == 1

    #проверяем метод установки жанра для книги
    def test_set_book_genre_valid_genre(self,b_collector):
        book_genre='Фантастика'
        book_name='Солярис'
        b_collector.add_new_book(book_name)
        b_collector.set_book_genre(book_name, book_genre)
        assert b_collector.get_book_genre(book_name) == book_genre

    #проверяем метод поиска книг по жанру
    def test_get_books_with_specific_genre_valid_search(self,b_collector):
        books = [
            ("Солярис", "Фантастика"),
            ("Звездные войны", "Фантастика"),
            ("Такси", "Комедии"),
            ("Оно", "Ужасы"),
        ]
        genre_for_search = 'Фантастика'
        for (book_name,book_genre) in books:
            b_collector.add_new_book(book_name)
            b_collector.set_book_genre(book_name, book_genre)  
        searching_book = b_collector.get_books_with_specific_genre(genre_for_search)
        assert "Солярис" in searching_book
        assert "Звездные войны" in searching_book    
        assert "Такси" not in searching_book       
        assert "Оно" not in searching_book       
        assert len(searching_book)==2

    #проверяем работу метода поиска книг для детей
    def test_get_books_for_children_valid_search(self,b_collector):
        books = [
            ("Солярис", "Фантастика"),
            ("Звездные войны", "Фантастика"),
            ("Такси", "Комедии"),
            ("Оно", "Ужасы"),
        ]
        for (book_name,book_genre) in books:
            b_collector.add_new_book(book_name)
            b_collector.set_book_genre(book_name, book_genre)  
        searching_book_for_children = b_collector.get_books_for_children()
        assert "Солярис" in searching_book_for_children
        assert "Звездные войны" in searching_book_for_children    
        assert "Такси"  in searching_book_for_children       
        assert  "Оно" not in searching_book_for_children       
        assert len(searching_book_for_children)==3

    #проверяем добавление книги в избранное
    def test_add_book_in_favorites_valid_append(self,b_collector):
        book_genre='Фантастика'
        book_name='Солярис'
        b_collector.add_new_book(book_name)
        b_collector.set_book_genre(book_name, book_genre)
        b_collector.add_book_in_favorites(book_name)
        favor_books = b_collector.get_list_of_favorites_books()

        assert book_name in favor_books
        assert len(favor_books) == 1

    #проверяем что не добавится двух одинаковых книг в избранное
    def test_add_book_in_favorites_two_same_books_not_append(self,b_collector):
        book_genre='Фантастика'
        book_name='Солярис'
        b_collector.add_new_book(book_name)
        b_collector.set_book_genre(book_name, book_genre)
        b_collector.add_book_in_favorites(book_name)
        b_collector.add_book_in_favorites(book_name)
        favor_books = b_collector.get_list_of_favorites_books()

        assert book_name in favor_books
        assert len(favor_books) == 1

    #проверяем удаление книги из избранного
    def test_delete_book_from_favorites_valid_delete(self,b_collector):
        book_genre='Фантастика'
        book_name='Солярис'
        b_collector.add_new_book(book_name)
        b_collector.set_book_genre(book_name, book_genre)
        b_collector.add_book_in_favorites(book_name)
        b_collector.delete_book_from_favorites(book_name)
        favor_books = b_collector.get_list_of_favorites_books()

        assert book_name not in favor_books
        assert len(favor_books) == 0

    #проверяем что добавленная книга существует
    def test_get_book_genre_existing_book(self, b_collector):
        book_name = "Солярис"
        book_genre = "Фантастика"
        b_collector.add_new_book(book_name)
        b_collector.set_book_genre(book_name, book_genre)
        result = b_collector.get_book_genre(book_name)
        assert result == book_genre

    # проверяем метод получения словаря фильмов целиком
    def test_get_books_genre_valid_dictionary(self, b_collector):
        books = [
            ("Солярис", "Фантастика"),
            ("Звездные войны", "Фантастика"),
            ("Такси", "Комедии"),
            ("Оно", "Ужасы"),
        ]
        expected_dict = dict(books)
        for (book_name,book_genre) in books:
            b_collector.add_new_book(book_name)
            b_collector.set_book_genre(book_name, book_genre)  
        result = b_collector.get_books_genre()
        assert result == expected_dict
