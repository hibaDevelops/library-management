from __init__ import db

from app.Models.BaseModel import BaseModel


class Author(BaseModel, db.Model):
    __tablename__ = "authors"

    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Author {self.name}>'
