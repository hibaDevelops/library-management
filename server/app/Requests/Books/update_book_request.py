from app.Requests import RequestInterface


class UpdateBookRequest(RequestInterface):
    def __init__(self):
        super().__init_subclass__()

    def init_parser(self):
        self.parser.add_argument(
            "name",
            type=str,
            store_missing=False,
            required=False
        )
        self.parser.add_argument(
            "author_id",
            type=int,
            store_missing=False,
            required=False
        )
        self.parser.add_argument(
            "publisher_id",
            type=int,
            store_missing=False,
            required=False
        )
        self.parser.add_argument(
            "available_copies_in_library",
            type=int,
            store_missing=False,
            required=False
        )
        self.parser.add_argument(
            "available_copies_for_sale",
            type=int,
            store_missing=False,
            required=False
        )
        self.parser.add_argument(
            "price",
            type=float,
            store_missing=False,
            required=False
        )
        self.parser.add_argument(
            "library_location",
            type=str,
            store_missing=False,
            required=False
        )
        self.parser.add_argument(
            "bookstore_location",
            type=str,
            store_missing=False,
            required=False
        )
        self.parser.add_argument(
            "language",
            type=str,
            store_missing=False,
            required=False
        )
        self.parser.add_argument(
            "photo",
            type=str,
            store_missing=False,
            required=False
        )
