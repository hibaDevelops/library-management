from app.Enums.SaleStatusEnum import validated_sale_status
from app.Requests import RequestInterface


class CreateSaleRequest(RequestInterface):
    def __init__(self):
        super().__init_subclass__()

    def init_parser(self):
        self.parser.add_argument(
            "client_id",
            type=int,
            store_missing=False,
            required=True
        )
        self.parser.add_argument(
            "book_id",
            type=int,
            store_missing=False,
            required=True
        )
        self.parser.add_argument(
            "sale_date",
            type=str,
            store_missing=False,
            required=True
        )
        self.parser.add_argument(
            "quantity",
            type=int,
            store_missing=False,
            required=True
        )
        self.parser.add_argument(
            "discount",
            type=float,
            store_missing=False,
            required=False
        )
        self.parser.add_argument(
            "status",
            type=validated_sale_status,
            store_missing=False,
            required=True
        )
