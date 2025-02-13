from flask_injector import FlaskInjector

from __init__ import api, app
from app.Controllers.Books.find_book_by_id_controller import FindBookByIdResource
from app.Controllers.Books.list_books_controller import ListBooksResource
from app.bindings.database import Database
from app.bindings.repositories import repositories
from app.bindings.services import services

api.add_resource(
    ListBooksResource,
    "/api/v1/books",
    methods=["GET"],
    endpoint="list_books"
)

api.add_resource(
    FindBookByIdResource,
    "/api/v1/books/<string:book_id>",
    methods=["GET"],
    endpoint="find_book_by_id"
)

injector = FlaskInjector(app=app, modules=[services, repositories, Database])
