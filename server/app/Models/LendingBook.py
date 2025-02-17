from __init__ import db
from app.Models.BaseModel import BaseModel


class LendingBook(BaseModel, db.Model):
    __tablename__ = 'lending_books'

    lending_id = db.Column(db.Integer, db.ForeignKey('lendings.id', ondelete='CASCADE'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id', ondelete='CASCADE'), nullable=False)

    # Relationships
    lending = db.relationship('Lending', backref=db.backref('lending_books', lazy=True))
    book = db.relationship('Book', backref=db.backref('lending_books', lazy=True))

    def __repr__(self):
        return f"<LendingBooks {self.id} - Lending {self.lending_id} - Book {self.book_id}>"


from app.Models.Lending import Lending  # noqa
from app.Models.Book import Book  # noqa
