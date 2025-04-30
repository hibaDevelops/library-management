from flask_injector import inject

from app.Models.Lending import Lending
from app.Repositories.ClientRepository import ClientRepository


class FindClientByIDService:
    @inject
    def __init__(
        self,
        client_repository: ClientRepository
    ):
        self.client_repository = client_repository

    def get(self, client_id: int) -> Lending | None:
        return self.client_repository.get_by_id(client_id)
