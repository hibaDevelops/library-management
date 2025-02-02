from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from configurations.config import Config
from database import MySQLDB


db = MySQLDB()
api = None

def create_app():
    flask = Flask(__name__)
    flask.config.from_object(Config)
    CORS(flask, origins='*')  

    global api
    api = Api(flask)
    db.init_app(flask)
    api.init_app(flask)

    return flask

app = create_app()

import api