from flask import current_app as app
from flask_security import hash_password
from Backend.models import db

def create_data():
    # Create roles with detailed descriptions
    try:
        with db.session.begin():
            app.security.datastore.find_or_create_role(name='Admin', description='Responsible for managing the entire application.')
            app.security.datastore.find_or_create_role(name='User', description="Utilize the application's primary features.")
            app.security.datastore.find_or_create_role(name='NotDecided', description='Till now we have two main roles.')
    except Exception as e:
        print(f"An error occurred: {e}")

    # Create user with the role
    try:
        with db.session.begin():
            if not app.security.datastore.find_user(email='admin@example.com'):
                app.security.datastore.create_user(email='admin@example.com',password=hash_password("123"), roles=['Admin'])

            if not app.security.datastore.find_user(email='user01@example.com'):
                app.security.datastore.create_user(email='user01@example.com',password=hash_password("123"), roles=['User'])

            if not app.security.datastore.find_user(email='user02@example.com'):
                app.security.datastore.create_user(email='user02@example.com',password=hash_password("123"), roles=['User'])
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.session.remove()

