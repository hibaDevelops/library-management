from flask_injector import inject

from app.Repositories.LendingRepository import LendingRepository


class ListLendingsService:
    @inject
    def __init__(
        self,
        lending_repository: LendingRepository
    ):
        self.lending_repository = lending_repository

    def list(self):
        return self.lending_repository.list_lendings()
