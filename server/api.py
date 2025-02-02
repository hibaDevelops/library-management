from flask_injector import FlaskInjector
from __init__ import api, app
from app.Controllers.Books.books_controller import BooksResource
from app.bindings.services import services
from app.bindings.repositories import repositories
from app.bindings.database import Database

api.add_resource(
    BooksResource,
    "/api/v1/books", 
    methods=['GET']
)

injector = FlaskInjector(app=app, modules=[services, repositories, Database])
