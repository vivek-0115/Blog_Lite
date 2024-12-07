from flask import Flask
from flask_security import SQLAlchemyUserDatastore, Security, hash_password,auth_required
from flask_cors import CORS

# Imports from Backends
from Backend.config import LocalDevelopmentConfig
from Backend.create_initial_data import create_data
from Backend.resourceApi import api
from Backend.models import *

def createApp():
    app=Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)
    datastore=SQLAlchemyUserDatastore(db, User, Role)
    app.security=Security(app, datastore, register_blueprint=False)
    CORS(app)
    db.init_app(app)
    api.init_app(app)
    app.app_context().push()
    return app

app = createApp()

with app.app_context():
    db.create_all()
    create_data()

#Routes #Routes #Routes #Routes
from Backend.routes import *

if (__name__ == "__main__"):
    app.run(debug=True)