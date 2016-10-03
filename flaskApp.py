import os
import sqlite3
from flask import Flask, request, render_template, \
    session, g, redirect, url_for, abort, flash, Markup
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime


def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)
    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'flaskr.db'),
        SECRET_KEY='development key',
        USERNAME='admin',
        PASSWORD='default'
    ))
    Bootstrap(app)
    Moment(app)
    return app

app = create_app()


@app.route('/')
def index(): return render_template('index.html', name='stranger', current_time=datetime.utcnow())


@app.route('/bootstrap/<name>')
def bootstrap(name): return render_template('base.html', name=name)


@app.route('/get/', methods=['GET', 'POST'])
def get():
    if request.method == 'GET':
        return 'GET method'
    else:
        return 'POST method'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()
