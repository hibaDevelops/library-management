from flask import Response, jsonify
from flask_injector import inject
from flask_restful import Resource

from app.Exceptions.not_found_exception import NotFoundException
from app.Services.Sales.FindSaleByIDService import FindSaleByIDService
from app.transformers.SaleTransformer import SaleTransformer


class FindSaleByIdResource(Resource):
    @inject
    def __init__(self, find_sale_by_id_service: FindSaleByIDService):
        self.find_sale_by_id_service = find_sale_by_id_service

    def get(self, sale_id: int) -> Response:
        sale = self.find_sale_by_id_service.get(sale_id)
        if sale is None:
            raise NotFoundException(f"No Sale found with id {sale_id}")
        else:
            sale_dto = SaleTransformer.transform(sale)
            return jsonify(sale_dto)
