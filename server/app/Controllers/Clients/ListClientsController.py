from flask import jsonify
from flask_injector import inject
from flask_restful import Resource

from app.Services.Clients.ListClientsService import ListClientsService
from app.transformers.ClientTransformer import ClientTransformer


class ListClientsResource(Resource):
    @inject
    def __init__(self, list_clients_service: ListClientsService):
        self.list_clients_service = list_clients_service

    def get(self):
        clients = self.list_clients_service.list()
        clients_dto = []
        for client in clients:
            client_dto = ClientTransformer.transform(client)
            clients_dto.append(client_dto)
        return jsonify({'clients': clients_dto})
