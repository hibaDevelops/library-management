from __init__ import db
from app.Models.BaseModel import BaseModel


class Lending(BaseModel, db.Model):
    __tablename__ = 'lendings'

    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    lent_date = db.Column(db.Date, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date)
    status = db.Column(db.Enum('active', 'returned', name='lending_status_enum'), nullable=False)

    # Relationships
    client = db.relationship('Client', backref='lendings', lazy=True)
    book = db.relationship('Book', backref='lendings', lazy=True)

    def __repr__(self):
        return f"<Lending {self.id} - Client {self.client_id} - Book {self.book_id}"


from app.Models.Client import Client  # noqa
from app.Models.Book import Book  # noqa
