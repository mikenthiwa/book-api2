from flask import jsonify, Blueprint
from flask_restplus import Resource, Api, reqparse
from models import model


book = model.Books()


class Books(Resource):
    """endpoint = /api/v1/books
       Methods = [GET, POST]"""
    req_data = reqparse.RequestParser()

    req_data.add_argument('book_id', type=int, required=True,
                          help='book_id is not provided', location=['json'])

    req_data.add_argument('title', type=str, required=True,
                          help='book title is not provided', location=['json'])

    req_data.add_argument('author', type=str, required=True,
                          help='book author is not provided', location=['json'])

    req_data.add_argument('copies', type=int, required=True, help='book copies is not provided', location=['json'])

    def get(self):
        return jsonify(book.get_books())

    def post(self):
        args = self.req_data.parse_args()
        book_id = args['book_id']
        title = args['title']
        author = args['author']
        copies = args['copies']

        return book.post_book(book_id, title, author, copies)


class Book(Resource):
    """endpoint /api/v1/book/<int:book_id
       methods = [GET, POST, PUT, DELETE]"""
    req_data = reqparse.RequestParser()
    req_data.add_argument('title', type=str, required=False, location=['json'])

    req_data.add_argument('author', type=str, required=False, location=['json'])

    req_data.add_argument('copies', type=str, location=['json'])

    def get(self, book_id):
        return jsonify(book.get_book(book_id))

    def put(self, book_id):
        args = self.req_data.parse_args()
        title = args['title']
        author = args['author']
        copies = args['copies']

        if title:
            return jsonify(book.modify_book_title(book_id, title))

        if author:
            return jsonify(book.modify_book_author(book_id, author))

        if copies:
            return jsonify(book.modify_book_copies(book_id, copies))

    def delete(self, book_id):
        return jsonify(book.delete_book(book_id))


books_api = Blueprint('resources.books', __name__)
api = Api(books_api)
api.add_resource(Books,
                 '/books',
                 endpoint='books')

api.add_resource(Book,
                 '/books/<int:book_id>',
                 endpoint='book')
