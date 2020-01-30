from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import AuthForm_login, AuthForm_create_account

@app.route("/auth/login", methods = [ "GET", "POST" ])
def auth_login():
    if request.method == "GET":
        return render_template("auth/login.html", form = AuthForm_login())
    
    form = AuthForm_login(request.form)
    
    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/login.html", form = form,
                                error = "No such username or password")
    
    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/create_account", methods = [ "GET" ])
def auth_create_account():
    return render_template("auth/create_account.html", form = AuthForm_create_account())

@app.route("/auth/create_account", methods = [ "POST" ])
def auth_add_account():
    form = AuthForm_create_account(request.form)
    
    if not form.validate():
        return render_template("auth/create_account.html", form = form)
    
    new_user = User(form.name.data, form.username.data, form.password.data)
    
    db.session().add(new_user)
    db.session().commit()
    
    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    login_user(user)
    
    return redirect(url_for("index"))
    