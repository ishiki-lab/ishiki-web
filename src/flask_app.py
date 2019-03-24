import os
from flask import Flask, g, render_template
from flask import send_from_directory

import config

app = Flask(__name__)

app.secret_key = config.FLASK_SECRET_KEY


def render_personalised_template(*args, **kwargs):
    kwargs["person"] = None

    return render_template(*args, **kwargs)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')