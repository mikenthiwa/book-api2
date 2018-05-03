class Books:
    def __init__(self):
        self.books = {1: [{"Title": "Harry Potter and Chamber of Secrets", "Author": "J.K Rowling", "Copies": 2}],
                      2: [{"Title": "Lone Wolf", "Author": "David Archer", "Copies": 3}]
                      }

    def details(self, book_id):
        book_details = self.books[book_id][0]
        return book_details

    def get_books(self):
        return self.books

    def get_book(self, book_id):
        return self.books[int(book_id)]

    def post_book(self, book_id, title, author, copies):
        new_book = self.books[book_id] = [{"Title": title, "Author": author, "Copies": copies}]
        return new_book

    def modify_book_title(self, book_id, title):
        book_details = self.books[book_id][0]
        book_details["Title"] = title
        return self.get_book(book_id)

    def modify_book_author(self, book_id, author):
        book_details = self.details(book_id)
        book_details["Author"] = author
        return self.get_book(book_id)

    def modify_book_copies(self, book_id, copies):
        book_details = self.details(book_id)
        book_details["Copies"] = copies
        return self.get_book(book_id)

    def delete_book(self, book_id):
        del self.books[book_id]
        return self.books



class Users:
    def __init__(self):
        self.users = {"mike.nthiwa": [{"email": "mike.nthiwa@gmail.com", "password": "123456789"}],
                      "regina.nthiwa": [{"email": "reg.nthiwa@gmail.com", "password": "987456123"}]
                      }

    def get_users(self):
        return self.users
