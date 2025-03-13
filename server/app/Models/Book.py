from __init__ import db

from app.Models.BaseModel import BaseModel


class Book(BaseModel, db.Model):
    __tablename__ = "books"

    name = db.Column(db.String(255), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
    publisher_id = db.Column(db.Integer, db.ForeignKey("publishers.id"))
    available_copies_in_library = db.Column(db.Integer, nullable=False)
    available_copies_for_sale = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, default=0.00)
    library_location = db.Column(db.String(255))
    bookstore_location = db.Column(db.String(255))
    language = db.Column(db.String(255))
    photo = db.Column(db.String(255))

    # Relationships (optional)
    author = db.relationship("Author", backref="books", passive_deletes=True)
    publisher = db.relationship("Publisher", backref="books", passive_deletes=True)
    lending = db.relationship('Lending', backref='books', lazy=True)

    def __repr__(self):
        return f'<Book {self.name}>'


from app.Models.Author import Author  # noqa
from app.Models.Publisher import Publisher  # noqa
from app.Models.Lending import Lending  # noqa
