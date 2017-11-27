import logging
from flask import Flask, render_template, request
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from datetime import datetime

app = Flask(__name__)
moment = Moment(app)
Bootstrap(app)

@app.route('/form')
def form():
    return render_template('form.html', timestamp = datetime.utcnow())

@app.route('/')
def index():
    return render_template('index.html',timestamp = datetime.utcnow())

@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['siteurl']
    comments = request.form['comments']

    return render_template(
        'submittedform.html',
        name=name,
        email=email,
        site=site,
        comments=comments,timestamp = datetime.utcnow())

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
