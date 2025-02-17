from flask import jsonify
from flask_injector import inject
from flask_restful import Resource

from app.Requests.Lendings.CreateLendingRequest import CreateLendingRequest
from app.Services.Lendings.CreateLendingService import CreateLendingService
from app.transformers.LendingTransformer import LendingTransformer


class CreateLendingResource(Resource):
    @inject
    def __init__(self, create_lending_service: CreateLendingService):
        self.create_lending_service = create_lending_service

    def post(self):
        request = CreateLendingRequest().get_data()
        lending = self.create_lending_service.create(**request)
        lending_dto = LendingTransformer.transform(lending)
        return jsonify(lending_dto)
