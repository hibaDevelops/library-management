from flask import Response, jsonify
from flask_injector import inject
from flask_restful import Resource

from app.Requests.Books.update_book_request import UpdateBookRequest
from app.Services.Books.UpdateBookByIDService import UpdateBookByIDService
from app.transformers.BookTransformer import BookTransformer


class UpdateBookByIdResource(Resource):
    @inject
    def __init__(self, update_book_by_id_service: UpdateBookByIDService):
        self.update_book_by_id_service = update_book_by_id_service

    def put(self, book_id: int) -> Response:
        request = UpdateBookRequest().get_data()
        book = self.update_book_by_id_service.update(book_id, **request)
        book_dto = BookTransformer.transform(book)
        return jsonify(book_dto)
