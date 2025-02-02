from __init__ import db
from database import MySQLDB
from injector import Module, provider, singleton

class Database(Module):
    @provider
    @singleton
    def describe(self) -> MySQLDB:
        return db
