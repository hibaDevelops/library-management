import os

class Config:
    DB_URI = os.environ.get("DATABASE_CONNECTION_URI")
