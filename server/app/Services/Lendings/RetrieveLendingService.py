from datetime import date

from flask_injector import inject
from sqlalchemy.exc import SQLAlchemyError

from app.Enums.LendingStatusEnum import LendingStatusEnum
from app.Exceptions.AlreadyReturnedException import AlreadyReturnedException
from app.Exceptions.not_found_exception import NotFoundException
from app.Models.Lending import Lending
from app.Repositories.BookRepository import BookRepository
from app.Repositories.LendingRepository import LendingRepository
from database import MySQLDB


class RetrieveLendingService:
    @inject
    def __init__(
        self,
        lending_repository: LendingRepository,
        book_repository: BookRepository,
        db: MySQLDB
    ):
        self.lending_repository = lending_repository
        self.book_repository = book_repository
        self.db = db

    def retrieve(self, lending_id: int) -> Lending:
        try:
            lending = self.lending_repository.get_by_id(lending_id)
            if not lending:
                raise NotFoundException(f"Lending with ID {lending_id} does not exist")

            if lending.status == LendingStatusEnum.RETURNED.value:
                raise AlreadyReturnedException(f"Lending with ID {lending.id} has already been returned.")

            book = lending.book
            if not book:
                raise NotFoundException(f"No Book found for this Lending ID {lending_id}")

            client = lending.client
            if not client:
                raise NotFoundException(f"No Client found for this Lending ID {lending_id}")

            update_fields = {'available_copies_in_library': book.available_copies_in_library + 1}
            self.book_repository.update(book, update_fields)

            lending.status = LendingStatusEnum.RETURNED.value
            lending.return_date = date.today()

            self.db.session.commit()

        except SQLAlchemyError as e:
            self.db.session.rollback()
            raise e
        except Exception as e:
            self.db.session.rollback()
            raise e

        return lending
