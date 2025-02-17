from typing import List

from flask_injector import inject

from app.Models.Book import Book
from database import MySQLDB


class BookRepository:
    @inject
    def __init__(self, db: MySQLDB):
        self.db = db

    def list_books(self) -> List[Book]:
        stm = self.db.select(Book).filter(Book.deleted_at == None).order_by(Book.name)
        return self.db.session.scalars(stm).all()

    def get_by_id(self, book_id: int) -> Book | None:
        stm = self.db.select(Book).filter(Book.id == book_id, Book.deleted_at == None).order_by(Book.name)
        return self.db.session.scalar(stm)

    def create(
        self,
        name,
        available_copies_in_library,
        available_copies_for_sale,
        price,
        location,
        author_id,
        publisher_id
    ) -> Book | None:
        new_book = Book(
            name=name,
            available_copies_in_library=available_copies_in_library,
            available_copies_for_sale=available_copies_for_sale,
            price=price,
            location=location,
            author_id=author_id,
            publisher_id=publisher_id
        )
        try:
            self.db.session.add(new_book)
            self.db.session.commit()
            return new_book
        except Exception as e:
            self.db.session.rollback()
            raise RuntimeError("An unexpected error occurred while creating the book.") from e

    def update(self, book: Book, update_fields: dict) -> Book:
        try:
            for field, value in update_fields.items():
                setattr(book, field, value)
            self.db.session.commit()
            return book
        except Exception as e:
            self.db.session.rollback()
            raise RuntimeError("An unexpected error occurred while updating the book.") from e
