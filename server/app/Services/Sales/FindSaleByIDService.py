from flask_injector import inject

from app.Models.Lending import Lending
from app.Repositories.SaleRepository import SaleRepository


class FindSaleByIDService:
    @inject
    def __init__(
        self,
        sale_repository: SaleRepository
    ):
        self.sale_repository = sale_repository

    def get(self, sale_id: int) -> Lending | None:
        return self.sale_repository.get_by_id(sale_id)
