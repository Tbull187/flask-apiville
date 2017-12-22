from flask import Flask, request, render_template
from flask_scss import Scss

app = Flask(__name__)
app.debug = True
Scss(app, static_dir='static', asset_dir='assets')

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

# app.run(debug=True, host='0.0.0.0', port=5000)