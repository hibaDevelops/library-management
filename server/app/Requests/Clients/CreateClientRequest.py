from app.Requests import RequestInterface


class CreateClientRequest(RequestInterface):
    def __init__(self):
        super().__init_subclass__()

    def init_parser(self):
        self.parser.add_argument(
            "firstname",
            type=str,
            store_missing=False,
            required=True
        )
        self.parser.add_argument(
            "lastname",
            type=str,
            store_missing=False,
            required=False
        )
        self.parser.add_argument(
            "phone",
            type=str,
            store_missing=False,
            required=True
        )
        self.parser.add_argument(
            "email",
            type=str,
            store_missing=False,
            required=False
        )
