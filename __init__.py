#All the necessary imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

#Initialization of the Flask application
app = Flask(__name__)

#Setting the system variables for the Flask application
app.config['SECRET_KEY'] = 'a74f31f72fe05b0f9689404dca465e86'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#Initialization of the database instance as well as the password hashing class
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#This import is specifically placed here to avoid circular imports
from Coronaweb import routes