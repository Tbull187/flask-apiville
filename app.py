from flask import Flask, request, render_template, redirect, url_for, make_response
from flask_scss import Scss
import json

app = Flask(__name__)
app.debug = True
Scss(app, static_dir='static', asset_dir='assets')


def get_saved_data():
    try:
        data =json.loads(request.cookies.get('sign-up'))
    except TypeError:
        data = {}
        return data    


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
    return render_template('sign-up.html')
###############################################

@app.route('/save', methods=['POST'])
def save():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('sign-up', json.dumps(dict(request.form.items())))
    return response


app.run(debug=True, host='0.0.0.0', port=5000)