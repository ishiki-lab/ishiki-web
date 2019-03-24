from flask import redirect, request, url_for, flash, render_template

import flask_app
from flask_app import app, render_personalised_template



@app.route('/', methods=['GET'])
def hello():
    print("hello")
    return render_personalised_template('home.html')
