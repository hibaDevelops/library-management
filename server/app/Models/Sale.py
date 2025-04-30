from __init__ import db
from app.Models.BaseModel import BaseModel


class Sale(BaseModel, db.Model):
    __tablename__ = 'sales'

    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    sale_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date)
    status = db.Column(db.Enum('cash_in_hand', 'processed', 'returned', name='sale_status_enum'), nullable=False)
    total_discount = db.Column(db.Float, default=0.00)

    # Relationships
    client = db.relationship('Client', backref='sales', lazy=True)
    books = db.relationship('Book', secondary='sale_books', backref=db.backref('sales_association', lazy=True))

    def __repr__(self):
        return f"<Sale {self.id} - Client {self.client_id}"


from app.Models.Client import Client  # noqa
from app.Models.Book import Book  # noqa
