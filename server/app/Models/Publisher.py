from __init__ import db

from app.Models.BaseModel import BaseModel


class Publisher(BaseModel, db.Model):
    __tablename__ = "publishers"

    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Publisher {self.name}>'
