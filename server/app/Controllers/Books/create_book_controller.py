from flask import jsonify
from flask_injector import inject
from flask_restful import Resource

from app.Requests.Books.create_book_request import CreateBookRequest
from app.Services.Books.CreateBookService import CreateBookService
from app.transformers.BookTransformer import BookTransformer


class CreateBookResource(Resource):
    @inject
    def __init__(self, create_book_service: CreateBookService):
        self.create_book_service = create_book_service

    def post(self):
        request = CreateBookRequest().get_data()
        book = self.create_book_service.create(**request)
        book_dto = BookTransformer.transform(book)
        return jsonify(book_dto)
