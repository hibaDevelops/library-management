from flask_injector import inject

from app.Repositories.SaleRepository import SaleRepository


class ListSalesService:
    @inject
    def __init__(
        self,
        sales_repository: SaleRepository
    ):
        self.sales_repository = sales_repository

    def list(self):
        return self.sales_repository.list_sales()
