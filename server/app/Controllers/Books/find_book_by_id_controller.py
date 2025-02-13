from flask import Response, jsonify
from flask_injector import inject
from flask_restful import Resource

from app.Exceptions.not_found_exception import NotFoundException
from app.Services.Books.FindBookByIdService import FindBookByIdService
from app.transformers.BookTransformer import BookTransformer


class FindBookByIdResource(Resource):
    @inject
    def __init__(self, find_book_by_id_service: FindBookByIdService):
        self.find_book_by_id_service = find_book_by_id_service

    def get(self, book_id: int) -> Response:
        book = self.find_book_by_id_service.get(book_id)
        if book is None:
            raise NotFoundException(f"No Book found with id {book_id}")
        else:
            book_dto = BookTransformer.transform(book)
            return jsonify(book_dto)
