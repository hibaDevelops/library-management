from __init__ import db
from app.Models.BaseModel import BaseModel


class Lending(BaseModel, db.Model):
    __tablename__ = 'lendings'

    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    lent_date = db.Column(db.Date, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date)
    status = db.Column(db.Enum('active', 'returned', 'overdue', name='lending_status_enum'), nullable=False)

    # Relationships
    client = db.relationship('Client', backref='lendings', lazy=True)
    books = db.relationship('Book', secondary='lending_books', backref=db.backref('lendings_association', lazy=True))

    def __repr__(self):
        return f"<Lending {self.id} - Client {self.client_id}"


from app.Models.Client import Client  # noqa
from app.Models.Book import Book  # noqa
from app.Models.LendingBook import LendingBook  # noqa
