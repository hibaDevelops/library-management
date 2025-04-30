from flask_injector import inject

from app.Models.Lending import Lending
from app.Repositories.LendingRepository import LendingRepository


class FindLendingByIDService:
    @inject
    def __init__(
        self,
        lending_repository: LendingRepository
    ):
        self.lending_repository = lending_repository

    def get(self, lending_id: int) -> Lending | None:
        return self.lending_repository.get_by_id(lending_id)
