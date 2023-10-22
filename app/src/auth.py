from flask import Blueprint, render_template, redirect, url_for, request, flash
from models import User
from . import db

# create authentication blueprint for handling relevant routes (signup, login, logout, etc.)
auth = Blueprint('auth', __name__)

# Redirect to ".html"-less url address; might not be necessary
@auth.route('/login.html')
def redirectLogin():
    return redirect('/login', code = 302)   # Probably should change 302 redirect code later

@auth.route('/login')
def login():
    loggedIn = False       # Temp logged-in value for now, changes header appearance
    return render_template('login.html', logged_in = loggedIn)

@auth.route('/login', methods=['POST'])
def login_post():
    # retrieve inputted login details 
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False # remember login info for user if they choose this

    user = User.query.filter_by(email=email).first() # if email is inputted, check for the email in database

    # if the user does not exist or password is wrong, redirect back to login page
    if not user or not user.check_password(password):
        flash('Incorrect email or password.')
        return redirect(url_for('auth.login'))

    # redirect to profile page if login is successful
    return redirect(url_for('main.profile'))
