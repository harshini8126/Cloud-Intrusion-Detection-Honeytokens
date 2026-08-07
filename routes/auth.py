from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
from models.models import User

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password,password):

            login_user(user)

            if user.role == "admin":
                return redirect(url_for("admin.admin_dashboard"))

            return redirect(url_for("employee.dashboard"))

        flash("Invalid Username or Password")

    return render_template("login.html")
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
from models.models import User

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user:

            if check_password_hash(user.password, password):

                login_user(user)

                if user.role == "admin":
                    return redirect(url_for("admin.admin_dashboard"))

                elif user.role == "employee":
                    return redirect(url_for("employee.dashboard"))

        flash("Invalid Username or Password")

    return render_template("login.html")


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))