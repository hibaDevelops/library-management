from flask import Response, jsonify
from flask_injector import inject
from flask_restful import Resource

from app.Exceptions.not_found_exception import NotFoundException
from app.Services.Clients.FindClientByIDService import FindClientByIDService
from app.transformers.ClientTransformer import ClientTransformer


class FindClientByIdResource(Resource):
    @inject
    def __init__(self, find_client_by_id_service: FindClientByIDService):
        self.find_client_by_id_service = find_client_by_id_service

    def get(self, client_id: int) -> Response:
        client = self.find_client_by_id_service.get(client_id)
        if client is None:
            raise NotFoundException(f"No Client found with id {client_id}")
        else:
            client_dto = ClientTransformer.transform(client)
            return jsonify(client_dto)
