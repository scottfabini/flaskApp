import os
import sqlite3
from flask import Flask, request, render_template, \
    session, g, redirect, url_for, abort, flash, Markup
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from datetime import datetime

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    # validator Required checks that the form is not empty
    submit = SubmitField('Submit')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '2ED35C78BC8F58B54F83A291A1EE4'
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


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    print(form.validate_on_submit())
    return render_template('index.html', name=name, current_time=datetime.utcnow(), form=form)


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
