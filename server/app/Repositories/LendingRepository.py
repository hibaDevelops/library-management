from typing import List

from flask_injector import inject

from app.Enums.LendingStatusEnum import LendingStatusEnum
from app.Models.Lending import Lending
from database import MySQLDB


class LendingRepository:
    @inject
    def __init__(self, db: MySQLDB):
        self.db = db

    def list_lendings(self) -> List[Lending]:
        stm = self.db.select(Lending).filter(
            Lending.deleted_at == None
        ).order_by(Lending.status, Lending.due_date)
        return self.db.session.scalars(stm).all()

    def get_by_id(self, lending_id: int) -> Lending | None:
        stm = self.db.select(Lending).filter(Lending.id == lending_id, Lending.deleted_at == None)
        return self.db.session.scalar(stm)

    def lend(
        self,
        client_id: int,
        book_id: int,
        lent_date: str,
        due_date: str,
    ) -> Lending:
        new_lending = Lending(
            client_id=client_id,
            book_id=book_id,
            lent_date=lent_date,
            due_date=due_date,
            status=LendingStatusEnum.ACTIVE.value
        )
        try:
            self.db.session.add(new_lending)
            self.db.session.commit()
            return new_lending
        except Exception as e:
            self.db.session.rollback()
            raise RuntimeError("An unexpected error occurred while issuing the book.") from e
