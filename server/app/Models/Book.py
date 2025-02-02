from __init__ import db
from datetime import datetime


class Book(db.Model):
    __tablename__ = "books"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    # created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Name %r>' % self.name
