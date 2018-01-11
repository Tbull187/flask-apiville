# Instructions
* (optional) activate new python virtualenv
* $ pip install -r requirements.txt
* $ FLASK_APP=app/app.py flask run

## Libraries Used
* Flask
* Flask-Scss
* Flask-WTF
* Flask-SQLAlchemy
* Flask-Migrate

## Project Structure
* currently an instance config is used in the root but is not commited to git. It holds the SECRET_KEY and SQLALCHEMY_DATABASE_URI 
* application lives in /app
* scss files live in assets/scss and get automatically compiled to .css and placed in static/css courtesy of Flask-Scss