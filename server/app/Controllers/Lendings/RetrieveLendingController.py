from flask import Response, jsonify
from flask_injector import inject
from flask_restful import Resource

from app.Services.Lendings.RetrieveLendingService import RetrieveLendingService
from app.transformers.LendingTransformer import LendingTransformer


class RetrieveLendingResource(Resource):
    @inject
    def __init__(self, retrieve_lending_service: RetrieveLendingService):
        self.retrieve_lending_service = retrieve_lending_service

    def patch(self, lending_id: int) -> Response:
        lending = self.retrieve_lending_service.retrieve(lending_id)
        lending_dto = LendingTransformer.transform(lending)
        return jsonify(lending_dto)
