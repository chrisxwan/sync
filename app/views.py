from datetime import datetime
from flask import render_template, session, redirect, url_for, request
from .forms import SignUpForm, SignInForm
from .models import User
from app import db
from app import myapp 
from app import models
from app import forms 


@myapp.route('/')
def front():
	form = SignInForm()
	form.email.placeholder = "Email"
	return render_template('front.html', form=form)
    
@myapp.route('/new', methods=['GET', 'POST'])
def new():
    form = SignUpForm()
    if request.method == 'POST':
		user = User(email = request.form['email'], password=request.form['password'])
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('front'))
    return render_template('new.html', form=form)







