from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import Required, Email, Length

class SignUpForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    password_confirm = PasswordField('Confirm Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Create User')

class SignInForm(Form):
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('Keep me logged in')
	submit = SubmitField('Login')

