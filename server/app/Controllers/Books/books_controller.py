from flask_restful import Resource
from flask import jsonify
from app.Services.Books.ListAllBooksService import ListAllBooksService
from flask_injector import inject

class BooksResource(Resource):
    @inject
    def __init__(self, list_all_books_service: ListAllBooksService):
        self.list_all_books_service = list_all_books_service
        
    def get(self):
        books = self.list_all_books_service.list()
        return jsonify({'books': books})
