from http import HTTPStatus

from flask import jsonify
from werkzeug.exceptions import HTTPException


class NotFoundException(HTTPException):
    def __init__(self, description=None, code=None, http_status=HTTPStatus.NOT_FOUND):
        self.description = description or http_status.phrase
        self.code = code or http_status.value
        response = jsonify({"success": False, "message": self.description}), self.code
        super().__init__(description, response)
