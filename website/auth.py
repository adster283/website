from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
import random
from flask_login import login_user, login_required, logout_user, current_user, login_manager
from sqlalchemy.sql import func

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            pass
            salt = db.session.query(User.user_salt).filter(User.email == email).first()
            salt = salt[0]
            password = password + str(salt)
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Password was incorrect!", category="error")
        else:
            flash("Email does not exist!", category="error")

    return render_template("login.html", user=current_user)

@auth.route("/logout")
def logout():
    ticker = User.query.all()
    print(ticker)
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():

    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("email already exits.", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 3 characters long.", category="error")
        elif len(firstName) < 2:
            flash("First name must be greater than 1 characters long.", category="error")
        elif password1 != password2:
            flash("Passwords do not match.", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters long.", category="error")
        else:
            numbers = "0123456789"
            salt = ""
            for i in range(250):
                salt = salt + numbers[random.randint(0, len(numbers)-1)]
            print(salt)
            new_user = User(email = email, first_name = firstName, password = generate_password_hash(password1 + salt , method='sha256'), user_salt=salt, current_stock="intc")
            db.session.add(new_user)
            db.session.commit()
            flash("Account successfully created!.", category="success")
            login_user(new_user, remember=True)
            return redirect(url_for("views.home"))

    return render_template("sign_up.html", user=current_user)