from flask import Flask

# initialize the app
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

# app confiqurations - database and printing
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recipe.db"
app.config["SQLALCHEMY_ECHO"] = True

# initialize db object
db = SQLAlchemy(app)

from application import views

from application.ingredients import models
from application.ingredients import views

# create database tables
db.create_all();