from flask import Blueprint, request, render_template, make_response
from .forms import SignUpForm
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/how-it-works')
def howItWorks():
    return render_template('how-it-works.html')

@main.route('/products')
def product():
    return render_template('products.html')

@main.route('/plans')
def plans():
    return render_template('plans.html')

@main.route('/company')
def company():
    return render_template('company.html')

@main.route('/help')
def help():
    return render_template('help.html')

@main.route('/sign-in')
def signIn():
    return render_template('sign-in.html')

@main.route('/sign-up')
def signUp():
    form = SignUpForm()
    return render_template('sign-up.html', form=form)
