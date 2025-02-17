from typing import List

from flask_injector import inject

from app.Models.Client import Client
from database import MySQLDB


class ClientRepository:
    @inject
    def __init__(self, db: MySQLDB):
        self.db = db

    def get_by_id(self, client_id: int) -> Client | None:
        stm = self.db.select(Client).filter(Client.id == client_id, Client.deleted_at == None)
        return self.db.session.scalar(stm)

    def list_clients(self) -> List[Client]:
        stm = self.db.select(Client).filter(Client.deleted_at == None).order_by(Client.firstname, Client.lastname)
        return self.db.session.scalars(stm).all()
