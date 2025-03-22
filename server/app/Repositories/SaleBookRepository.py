from flask_injector import inject

from app.Models.SaleBook import SaleBook
from database import MySQLDB


class SaleBookRepository:
    @inject
    def __init__(self, db: MySQLDB):
        self.db = db

    def create(self, sale_id: int, book_id: int, quantity: int) -> SaleBook | None:
        new_sale_book = SaleBook(
            sale_id=sale_id,
            book_id=book_id,
            quantity=quantity
        )
        try:
            self.db.session.add(new_sale_book)
            self.db.session.commit()
            return new_sale_book
        except Exception as e:
            self.db.session.rollback()
            raise RuntimeError("An unexpected error occurred while making the sale.") from e
