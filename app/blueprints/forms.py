from flask import Blueprint, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

form_page = Blueprint('form_page', __name__)

class SignUpForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()], render_kw={'placeholder': 'Name'})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'Email'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'Password'})

@form_page.route('/submit', methods=['POST'])
def submit():
    form = SignUpForm()       
    # if  not form.validate():
    #     print('form not validated')
    #     flash('form not validated')
    
    # if form.errors:
    #     print(form.errors)
    #     flash('form error')

    if form.validate_on_submit():
        print('validated and submitted')
        return redirect(url_for('main.index'))
    return render_template('sign-up.html', form=form)