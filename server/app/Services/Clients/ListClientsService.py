from flask_injector import inject

from app.Repositories.ClientRepository import ClientRepository


class ListClientsService:
    @inject
    def __init__(
        self,
        client_repository: ClientRepository
    ):
        self.client_repository = client_repository

    def list(self):
        return self.client_repository.list_clients()
