from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


myapp = Flask(__name__)
myapp.config.from_object('config')


bootstrap = Bootstrap(myapp)
mail = Mail(myapp)
moment = Moment(myapp)
db = SQLAlchemy(myapp)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.init_app(myapp)

from app import views, models
