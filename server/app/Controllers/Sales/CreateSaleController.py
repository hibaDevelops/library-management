from flask import jsonify
from flask_injector import inject
from flask_restful import Resource

from app.Requests.Sales.CreateSaleRequest import CreateSaleRequest
from app.Services.Sales.CreateSaleService import CreateSaleService
from app.transformers.SaleTransformer import SaleTransformer


class CreateSaleResource(Resource):
    @inject
    def __init__(self, create_sale_service: CreateSaleService):
        self.create_sale_service = create_sale_service

    def post(self):
        request = CreateSaleRequest().get_data()
        sale = self.create_sale_service.create(**request)
        sale_dto = SaleTransformer.transform(sale)
        return jsonify(sale_dto)
