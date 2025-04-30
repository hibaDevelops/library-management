from flask import jsonify
from flask_injector import inject
from flask_restful import Resource

from app.Requests.Clients.CreateClientRequest import CreateClientRequest
from app.Services.Clients.CreateClientService import CreateClientService
from app.transformers.ClientTransformer import ClientTransformer


class CreateClientResource(Resource):
    @inject
    def __init__(self, create_client_service: CreateClientService):
        self.create_client_service = create_client_service

    def post(self):
        request = CreateClientRequest().get_data()
        client = self.create_client_service.create(**request)
        client_dto = ClientTransformer.transform(client)
        return jsonify(client_dto)
