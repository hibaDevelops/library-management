from flask_injector import inject
from sqlalchemy.exc import SQLAlchemyError

from app.Exceptions.OutOfStockException import OutOfStockException
from app.Exceptions.not_found_exception import NotFoundException
from app.Models.Lending import Lending
from app.Repositories.BookRepository import BookRepository
from app.Repositories.ClientRepository import ClientRepository
from app.Repositories.LendingRepository import LendingRepository
from database import MySQLDB


class CreateLendingService:
    @inject
    def __init__(
        self,
        lending_repository: LendingRepository,
        client_repository: ClientRepository,
        book_repository: BookRepository,
        db: MySQLDB
    ):
        self.lending_repository = lending_repository
        self.client_repository = client_repository
        self.book_repository = book_repository
        self.db = db

    def create(
        self,
        client_id: int,
        book_id: int,
        lent_date: str,
        due_date: str
    ) -> Lending:
        try:
            client = self.client_repository.get_by_id(client_id)
            if not client:
                raise NotFoundException(f"Client with ID {client_id} does not exist")

            book = self.book_repository.get_by_id(book_id)
            if not book:
                raise NotFoundException(f"Book with ID {book_id} does not exist")
            if book.available_copies_in_library == 0:
                raise OutOfStockException(f"This Book '{book.name}' is currently out of stock")

            lending = self.lending_repository.lend(
                client_id,
                book_id,
                lent_date,
                due_date
            )

            update_fields = {'available_copies_in_library': book.available_copies_in_library - 1}
            self.book_repository.update(book, update_fields)

            self.db.session.commit()

        except SQLAlchemyError as e:
            self.db.session.rollback()
            raise e
        except Exception as e:
            self.db.session.rollback()
            raise e

        return lending
