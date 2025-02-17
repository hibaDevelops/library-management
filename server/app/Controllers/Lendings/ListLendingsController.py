from flask import jsonify
from flask_injector import inject
from flask_restful import Resource

from app.Services.Lendings.ListLendingsService import ListLendingsService
from app.transformers.LendingTransformer import LendingTransformer


class ListLendingsResource(Resource):
    @inject
    def __init__(self, list_lendings_service: ListLendingsService):
        self.list_lendings_service = list_lendings_service

    def get(self):
        lendings = self.list_lendings_service.list()
        lendings_dto = []
        for lending in lendings:
            lending_dto = LendingTransformer.transform(lending)
            lendings_dto.append(lending_dto)
        return jsonify({'lendings': lendings_dto})
