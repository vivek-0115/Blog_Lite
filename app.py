from flask import Flask
from Backend.config import LocalDevelopmentConfig
from flask_security import SQLAlchemyUserDatastore, Security, hash_password,auth_required
from Backend.create_initial_data import create_data

from Backend.models import *

def createApp():
    app=Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)
    datastore=SQLAlchemyUserDatastore(db, User, Role)
    app.security=Security(app, datastore, register_blueprint=False)
    db.init_app(app)
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