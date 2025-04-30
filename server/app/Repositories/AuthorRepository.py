from flask_injector import inject

from app.Models.Author import Author
from database import MySQLDB


class AuthorRepository:
    @inject
    def __init__(self, db: MySQLDB):
        self.db = db

    def get_by_id(self, author_id: int) -> Author | None:
        stm = self.db.select(Author).filter(Author.id == author_id, Author.deleted_at == None)
        return self.db.session.scalar(stm)
