from datetime import datetime
from typing import List

from flask_injector import inject

from app.Models.Lending import Lending
from database import MySQLDB


class LendingRepository:
    @inject
    def __init__(self, db: MySQLDB):
        self.db = db

    def list_lendings(self) -> List[Lending]:
        stm = self.db.select(Lending).filter(
            Lending.deleted_at == None,
            Lending.due_date < datetime.now(),
            Lending.return_date == None
        ).order_by(Lending.due_date)
        return self.db.session.scalars(stm).all()
