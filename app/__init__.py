from app.helpers.restricted_admin import RestrictedAdminIndexView
from flask import Flask
from flask.ext.admin import Admin
from flask.ext.login import LoginManager
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

api_manager = APIManager(app, flask_sqlalchemy_db=db)
admin_manager = Admin(app,
                      index_view=RestrictedAdminIndexView(),
                      name='Site Administration'
                     )

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import commands, models, views
