from flask import jsonify
from flask_injector import inject
from flask_restful import Resource

from app.Services.Sales.ListSalesService import ListSalesService
from app.transformers.SaleTransformer import SaleTransformer


class ListSalesResource(Resource):
    @inject
    def __init__(self, list_sales_service: ListSalesService):
        self.list_sales_service = list_sales_service

    def get(self):
        sales = self.list_sales_service.list()
        sales_dto = []
        for sale in sales:
            sale_dto = SaleTransformer.transform(sale)
            sales_dto.append(sale_dto)
        return jsonify({'sales': sales_dto})
