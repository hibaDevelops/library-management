from app.Requests import RequestInterface


class CreateLendingRequest(RequestInterface):
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
            "lent_date",
            type=str,
            store_missing=False,
            required=True
        )
        self.parser.add_argument(
            "due_date",
            type=str,
            store_missing=False,
            required=True
        )
