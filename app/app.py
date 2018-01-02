from flask import Flask, request, render_template, redirect, url_for, make_response
from flask_scss import Scss
import json
# Forms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

app = Flask(__name__, instance_relative_config=True)
# default config and relative instance/config
app.config.from_object('config.default')
app.config.from_pyfile('config.py')
# set secret_key and static files
app.secret_key = app.config['SECERET_KEY']
# flask_scss config
Scss(app, static_dir='app/static', asset_dir='app/assets')   

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/how-it-works')
def howItWorks():
    return render_template('how-it-works.html')

@app.route('/products')
def product():
    return render_template('products.html')

@app.route('/plans')
def plans():
    return render_template('plans.html')

@app.route('/company')
def company():
    return render_template('company.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/sign-in')
def signIn():
    return render_template('sign-in.html')

@app.route('/sign-up')
def signUp():
    form = SignUpForm()
    return render_template('sign-up.html', form=form)
###############################################

# signUp form
class SignUpForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

@app.route('/save', methods=['POST'])
def save():
    form = SignUpForm()
    if form.validate_on_submit():
        print('form submitted')
        return redirect(url_for('index'))
    return render_template('sign-up.html', form=form)

app.run(debug=True, host='0.0.0.0', port=5000)