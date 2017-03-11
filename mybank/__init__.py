from flask import Flask

from flask_sqlalchemy import SQLAlchemy
#from flask.ext.bcrypt import Bcrypt
from flask_bcrypt import Bcrypt
#from flask.ext.login import LoginManager
from flask_login import LoginManager

app=Flask(__name__)
bcrypt = Bcrypt(app)
login_manager=LoginManager()
login_manager.init_app(app)

#config
app.config.from_object('config.DevelopmentConfig')
db =SQLAlchemy(app)

from models import User