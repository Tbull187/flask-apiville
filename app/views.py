from flask import request, render_template, make_response
from .app import app
from .forms import SignUpForm
import json


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
