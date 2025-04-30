from flask_injector import inject

from app.Models.Client import Client
from app.Repositories.ClientRepository import ClientRepository


class CreateClientService:
    @inject
    def __init__(
        self,
        client_repository: ClientRepository,
    ):
        self.client_repository = client_repository

    def create(
        self,
        firstname: str,
        phone: str,
        lastname: str = None,
        email: str = None
    ) -> Client:
        return self.client_repository.create(
            firstname,
            phone,
            lastname,
            email
        )
