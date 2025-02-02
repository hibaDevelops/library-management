from database import MySQLDB
from flask_injector import inject
from app.Models.Book import Book
from typing import List

class BookRepository:
    @inject
    def __init__(self, db: MySQLDB):
        self.db = db
        
    def list_books(self) -> List[Book]:
        stm = self.db.select(Book).order_by(Book.name)
        return self.db.session.scalars(stm).all()
