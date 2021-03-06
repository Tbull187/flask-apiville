from flask import Flask
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, instance_relative_config=True)
# default config and relative instance/config
app.config.from_object('config.default')
app.config.from_pyfile('config.py')
# set secret_key
app.secret_key = app.config['SECERET_KEY']
# flask_scss config
Scss(app, static_dir='static', asset_dir='assets')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .forms import *
from .views import *
from .models import *
