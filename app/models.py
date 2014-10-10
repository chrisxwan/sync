from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String)
    password_hash = db.Column(db.String(128))

    @property 
    def password(self):
    	raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)  

    def __init__(self, email, password):
        self.email = email
        self.passowrd = password

