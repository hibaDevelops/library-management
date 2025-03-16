from __init__ import db
from app.Models.BaseModel import BaseModel


class SaleBook(BaseModel, db.Model):
    __tablename__ = 'sale_books'

    sale_id = db.Column(db.Integer, db.ForeignKey('sales.id', ondelete='CASCADE'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id', ondelete='CASCADE'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    # Relationships
    sale = db.relationship('Sale', backref=db.backref('sale_books', lazy=True))
    book = db.relationship('Book', backref=db.backref('sale_books', lazy=True))

    def __repr__(self):
        return f"<SaleBooks {self.id} - Sale {self.sale_id} - Book {self.book_id}>"


from app.Models.Sale import Sale  # noqa
from app.Models.Book import Book  # noqa
