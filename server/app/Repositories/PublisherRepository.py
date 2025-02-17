from flask_injector import inject

from app.Models.Publisher import Publisher
from database import MySQLDB


class PublisherRepository:
    @inject
    def __init__(self, db: MySQLDB):
        self.db = db

    def get_by_id(self, publisher_id: int) -> Publisher | None:
        stm = self.db.select(Publisher).filter(Publisher.id == publisher_id, Publisher.deleted_at == None)
        return self.db.session.scalar(stm)
