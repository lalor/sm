#!/usr/bin/python
#-*- coding: UTF-8 -*-
from flask_bootstrap import Bootstrap
from flask_login import login_required, login_user, logout_user

from flask import redirect, url_for, flash, Flask, request, render_template

from ext import db, login_manager
from forms import HostForm, LoginForm
from models import Host, User
from utils import format_rpc
import supervisor_rpc

app = Flask(__name__)
app.config.from_pyfile('settings.py')

bootstrap = Bootstrap(app)

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "login"


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        form = HostForm()
        if form.validate_on_submit():
            data = form.data
            host = Host(**data)
            db.session.add(host)
            db.session.commit()
        else:
            flash(form.errors)
        return redirect(url_for('index'))
    else:
        form = HostForm()
        hosts = Host.query.all()
        return render_template('index.html', hosts=hosts, form=form)


@app.route('/process/<host_id>')
@login_required
def process(host_id):

    rv = None
    action = request.args.get('action')
    process_name = request.args.get('process_name')

    host = Host.query.filter_by(id=host_id).first_or_404()
    rpc = format_rpc(host)
    if hasattr(supervisor_rpc, action):
        call = getattr(supervisor_rpc, action)
        rv = call(rpc=rpc, process_name=process_name)
    else:
        flash("invalid action")

    processes = supervisor_rpc.get_all_process_info(rpc)
    return render_template('process.html', processes=processes,
            host_id=host_id, message=rv)


@app.route('/delete/<int:host_id>', methods=['GET'])
@login_required
def delete_host(host_id):
    host = Host.query.filter_by(id=host_id).first_or_404()
    db.session.delete(host)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username'], password=request.form['password']).first()
        if user:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have logout!')
    return redirect(url_for('login'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()


@app.cli.command()
def init_db():
    """
    initialize database
    """
    with app.app_context():
        db.create_all()
        admin = User(username='admin', password='admin', email='admin@163.com')
        db.session.add(admin)
        db.session.commit()


@app.cli.command()
def drop_db():
    """
    warnings operation, drop database
    """
    with app.app_context():
        db.drop_all()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)
