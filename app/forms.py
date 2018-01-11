from flask import render_template, redirect, url_for, request
from .app import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

class SignUpForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()], render_kw={'placeholder': 'Name'})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'Email'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'Password'})

def create_user():
    pass

@app.route('/submit', methods=['POST'])
def submit():
    form = SignUpForm()       
    # if  not form.validate():
    #     print('form not validated')
    #     flash('form not validated')
    
    # if form.errors:
    #     print(form.errors)
    #     flash('form error')

    if request.method == 'POST' and form.validate_on_submit():
        print('validated and submitted')

        name = request.form['username']
        email = request.form['email']
        password = request.form['password']

        print(f'''
        username: {name}
        email: {email}
        password: {password}
        ''')

        return redirect(url_for('index'))
    return render_template('sign-up.html', form=form)