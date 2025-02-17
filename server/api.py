from flask_injector import FlaskInjector

from __init__ import api, app
from app.Controllers.Books.create_book_controller import CreateBookResource
from app.Controllers.Books.find_book_by_id_controller import FindBookByIdResource
from app.Controllers.Books.list_books_controller import ListBooksResource
from app.Controllers.Books.update_book_by_id_controller import UpdateBookByIdResource
from app.bindings.database import Database
from app.bindings.repositories import repositories
from app.bindings.services import services

# Book endpoints
api.add_resource(
    ListBooksResource,
    "/api/v1/books",
    methods=["GET"],
    endpoint="list_books"
)
api.add_resource(
    CreateBookResource,
    "/api/v1/books",
    methods=["POST"],
    endpoint="create_book"
)
api.add_resource(
    FindBookByIdResource,
    "/api/v1/books/<string:book_id>",
    methods=["GET"],
    endpoint="find_book_by_id"
)
api.add_resource(
    UpdateBookByIdResource,
    "/api/v1/books/<string:book_id>",
    methods=["PUT"],
    endpoint="update_book_by_id"
)

injector = FlaskInjector(app=app, modules=[services, repositories, Database])
