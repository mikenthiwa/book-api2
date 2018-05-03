import unittest
from models import model


class TestModels(unittest.TestCase):
    def setUp(self):
        self.book = model.Books()

    def test_get_books_method(self):
        """Test get all book method"""
        result = self.book.get_books()
        self.assertTrue(result)

    def test_get_specific_book_method(self):
        """Test get a book method"""
        # When book id is int
        book_id = 1
        result = self.book.get_book(book_id)
        self.assertEqual(result, [{"Title": "Harry Potter and Chamber of Secrets",
                                   "Author": "J.K Rowling",
                                   "Copies": 2}])

    def test_post_book_method(self):
        """Test post a book method"""
        book_id = 4
        title = "The Whistler"
        author = "John Grisham"
        copies = 3
        result = self.book.post_book(book_id, title, author, copies)
        self.assertEqual(result, [{"Title": "The Whistler",
                                   "Author": "John Grisham",
                                   "Copies": 3}])

    def test_details(self):
        """Testing function details"""
        book_id = 1
        result = self.book.get_books()[book_id][0]
        self.assertEqual(result, {"Title": "Harry Potter and Chamber of Secrets",
                                  "Author": "J.K Rowling", "Copies": 2})

    def test_modify_book_title_method(self):
        """Testing modify book information"""
        # modify book title
        book_id = 2
        book_title = "Lost Girl"
        result = self.book.modify_book_title(book_id, book_title)
        self.assertEqual(result, [{"Title": "Lost Girl",
                                   "Author": "David Archer",
                                   "Copies": 3}])

        # modify book author
        book_author = "Paulo Coelho"
        result = self.book.modify_book_author(2, book_author)
        self.assertEqual(result, [{"Title": book_title,
                                   "Author": book_author,
                                   "Copies": 3}])

        # modify book copies
        copies = 5
        result = self.book.modify_book_copies(book_id, copies)
        self.assertEqual(result, [{"Title": book_title,
                                   "Author": book_author,
                                   "Copies": copies}])

    def test_delete_method(self):
        book_id = 2
        all_books = self.book.get_books()
        self.book.delete_book(book_id)
        self.assertNotIn(book_id, all_books.keys())

if __name__ == '__main__':
    unittest.main()
