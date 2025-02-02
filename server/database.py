from flask_sqlalchemy import SQLAlchemy

class MySQLDB(SQLAlchemy):
    def __init__(self, app=None):
        super().__init__()
        
        if app is not None:
            self.init_app(app)
            
    def init_app(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = app.config["DB_URI"]
        super().init_app(app)
