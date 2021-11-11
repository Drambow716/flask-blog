# import flask 

from os import environ

from dotenv import load_dotenv

from flask import Flask

from flask_ckeditor import CKEditor

from src.db.db import db

from src.db.models.blog import Blogs

from src.routes.admin.blueprint import admin_blueprint

from src.routes.home.blueprint import home_blueprint

# create the application object

load_dotenv()


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DATABASE_URL")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True

db.init_app(app)

db.create_all(app=app)


ckeditor = CKEditor()

ckeditor.init_app(app)


app.register_blueprint(home_blueprint)

app.register_blueprint(admin_blueprint)



