from flask_injector import FlaskInjector

from __init__ import api, app
from app.Controllers.Books.create_book_controller import CreateBookResource
from app.Controllers.Books.find_book_by_id_controller import FindBookByIdResource
from app.Controllers.Books.list_books_controller import ListBooksResource
from app.Controllers.Books.update_book_by_id_controller import UpdateBookByIdResource
from app.Controllers.Clients.CreateClientController import CreateClientResource
from app.Controllers.Clients.FindClientByIDController import FindClientByIdResource
from app.Controllers.Clients.ListClientsController import ListClientsResource
from app.Controllers.Lendings.CreateLendingController import CreateLendingResource
from app.Controllers.Lendings.FindLendingByIDController import FindLendingByIdResource
from app.Controllers.Lendings.ListLendingsController import ListLendingsResource
from app.Controllers.Lendings.RetrieveLendingController import RetrieveLendingResource
from app.Controllers.Sales.CreateSaleController import CreateSaleResource
from app.Controllers.Sales.FindSaleByIdController import FindSaleByIdResource
from app.Controllers.Sales.ListSalesController import ListSalesResource
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

# Lending endpoints
api.add_resource(
    ListLendingsResource,
    "/api/v1/lendings",
    methods=["GET"],
    endpoint="list_lendings"
)
api.add_resource(
    CreateLendingResource,
    "/api/v1/lendings",
    methods=["POST"],
    endpoint="create_lending"
)
api.add_resource(
    FindLendingByIdResource,
    "/api/v1/lendings/<string:lending_id>",
    methods=["GET"],
    endpoint="find_lending_by_id"
)
api.add_resource(
    RetrieveLendingResource,
    "/api/v1/lendings/<string:lending_id>/retrieve",
    methods=["PATCH"],
    endpoint="retrieve_lent_book"
)

# Client endpoints
api.add_resource(
    ListClientsResource,
    "/api/v1/clients",
    methods=["GET"],
    endpoint="list_clients"
)
api.add_resource(
    CreateClientResource,
    "/api/v1/clients",
    methods=["POST"],
    endpoint="create_client"
)
api.add_resource(
    FindClientByIdResource,
    "/api/v1/clients/<string:client_id>",
    methods=["GET"],
    endpoint="find_client_by_id"
)

# Sales endpoints
api.add_resource(
    ListSalesResource,
    "/api/v1/sales",
    methods=["GET"],
    endpoint="list_sales"
)
api.add_resource(
    FindSaleByIdResource,
    "/api/v1/sales/<string:sale_id>",
    methods=["GET"],
    endpoint="find_sale_by_id"
)
api.add_resource(
    CreateSaleResource,
    "/api/v1/sales",
    methods=["POST"],
    endpoint="create_sale"
)

injector = FlaskInjector(app=app, modules=[services, repositories, Database])
