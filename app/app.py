from flask import Flask
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from .blueprints.views import main
from .blueprints.forms import form_page

app = Flask(__name__, instance_relative_config=True)
# default config and relative instance/config
app.config.from_object('config.default')
app.config.from_pyfile('config.py')
# set secret_key
app.secret_key = app.config['SECERET_KEY']
# flask_scss config
Scss(app, static_dir='app/static', asset_dir='app/assets')

db = SQLAlchemy(app)

app.register_blueprint(main)
app.register_blueprint(form_page)

app.run(debug=True, host='0.0.0.0', port=5000)