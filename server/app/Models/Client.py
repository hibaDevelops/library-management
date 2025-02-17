from __init__ import db
from app.Models.BaseModel import BaseModel


class Client(BaseModel, db.Model):
    __tablename__ = 'clients'

    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100))
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(255))

    def __repr__(self):
        return f"<Client {self.id}>"
