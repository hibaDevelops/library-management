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

    def get_by_id(self, sale_id: int) -> Sale | None:
        stm = self.db.select(Sale).filter(Sale.id == sale_id, Sale.deleted_at == None)
        return self.db.session.scalar(stm)

    def create(self, client_id: int, sale_date: str, status: str, discount: float) -> Sale | None:
        new_sale = Sale(
            client_id=client_id,
            sale_date=sale_date,
            status=status,
            total_discount=discount
        )
        try:
            self.db.session.add(new_sale)
            self.db.session.commit()
            return new_sale
        except Exception as e:
            self.db.session.rollback()
            raise RuntimeError("An unexpected error occurred while making the sale.") from e
