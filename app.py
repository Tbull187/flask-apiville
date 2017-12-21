from flask import Flask, request, render_template
from flask_scss import Scss

app = Flask(__name__)
app.debug = True
Scss(app, static_dir='static', asset_dir='assets')

@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True, host='0.0.0.0', port=5000)