from http import HTTPStatus

from flask import jsonify
from werkzeug.exceptions import HTTPException


class OutOfStockException(HTTPException):
    def __init__(self, description=None, code=None, http_status=HTTPStatus.BAD_REQUEST):
        self.description = description or http_status.phrase
        self.code = code or http_status.value
        response = jsonify({"success": False, "message": self.description}), self.code
        super().__init__(description, response)
