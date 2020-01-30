from flask import Flask

# initialize the app
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

#app configurations on different environments (Heroku & local)
if os.environ.get("HEROKU"):
    #Heroku database
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    #local database and printing
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recipe.db"
    app.config["SQLALCHEMY_ECHO"] = True

# initialize db object
db = SQLAlchemy(app)

# application specific imports
from application import views

from application.ingredients import models
from application.ingredients import views

from application.auth import models
from application.auth import views

# login functionality
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# create database tables
try:
    db.create_all()
except:
    pass