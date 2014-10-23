from app import app
from app import login_manager
from app.models.user import User
from flask import request, redirect, url_for, render_template, flash
from flask.ext.login import login_user

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    email = request.form['email']
    password = request.form['password']
    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
        login_user(user)
        flash('Logged in successfully')
        return redirect(request.args.get('next') or url_for('index'))
    else:
        flash('Username or Password is invalid', 'error')
        return redirect(url_for('login'))
    return redirect(url_for('index'))
