from flask import Response, jsonify
from flask_injector import inject
from flask_restful import Resource

from app.Exceptions.not_found_exception import NotFoundException
from app.Services.Lendings.FindLendingByIDService import FindLendingByIDService
from app.transformers.LendingTransformer import LendingTransformer


class FindLendingByIdResource(Resource):
    @inject
    def __init__(self, find_lending_by_id_service: FindLendingByIDService):
        self.find_lending_by_id_service = find_lending_by_id_service

    def get(self, lending_id: int) -> Response:
        lending = self.find_lending_by_id_service.get(lending_id)
        if lending is None:
            raise NotFoundException(f"No Lending found with id {lending_id}")
        else:
            lending_dto = LendingTransformer.transform(lending)
            return jsonify(lending_dto)
