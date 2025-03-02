from flask import jsonify
from flask_injector import inject
from flask_restful import Resource

from app.Services.Books.ListAllBooksService import ListAllBooksService
from app.transformers.BookTransformer import BookTransformer


class ListBooksResource(Resource):
    @inject
    def __init__(self, list_all_books_service: ListAllBooksService):
        self.list_all_books_service = list_all_books_service

    def get(self):
        books = self.list_all_books_service.list()
        books_dto = []
        for book in books:
            book_dto = BookTransformer.transform(book)
            books_dto.append(book_dto)
        return jsonify({'books': books_dto})
