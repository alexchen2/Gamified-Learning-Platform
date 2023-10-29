from flask import Flask, render_template
from flask_login import LoginManager
from models import db, User
from auth import auth as auth_blueprint


app = Flask(__name__)
# app.register_blueprint(auth)

# Configure and initalize database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)
db.init_app(app)

# register blueprint with authorization routes for the app
app.register_blueprint(auth_blueprint)

@login_manager.user_loader
def load_user(user_id):
    # retrieve the given user from database, user id is the primary key so it will query the correct user
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

with app.app_context():      # Need to add as of Flask-SQLAlchemy 3.0
    db.create_all()

