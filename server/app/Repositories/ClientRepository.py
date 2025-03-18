from typing import List

from flask_injector import inject

from app.Exceptions.UniqueConstraintViolationException import UniqueConstraintViolationException
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

    def create(
        self,
        firstname,
        phone,
        lastname,
        email
    ) -> Client:

        existing_client = Client.query.filter((Client.email == email) | (Client.phone == phone)).first()

        if existing_client:
            if existing_client.email == email:
                raise UniqueConstraintViolationException("Email is already in use")
            elif existing_client.phone == phone:
                raise UniqueConstraintViolationException("Phone number is already in use")

        new_client = Client(
            firstname=firstname,
            lastname=lastname,
            phone=phone,
            email=email
        )
        try:
            self.db.session.add(new_client)
            self.db.session.commit()
            return new_client
        except Exception as e:
            self.db.session.rollback()
            raise RuntimeError("An unexpected error occurred while creating the client.") from e
