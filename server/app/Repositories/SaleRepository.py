from typing import List

from flask_injector import inject

from app.Models.Sale import Sale
from database import MySQLDB


class SaleRepository:
    @inject
    def __init__(self, db: MySQLDB):
        self.db = db

    def list_sales(self) -> List[Sale]:
        stm = self.db.select(Sale).filter(
            Sale.deleted_at == None
        ).order_by(Sale.sale_date.desc())
        return self.db.session.scalars(stm).all()
