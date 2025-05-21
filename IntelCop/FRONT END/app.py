from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import pandas as pd
from config import Config
from models import db, User
from forms import RegistrationForm, LoginForm
from llm_api import query_llm
from flask import flash, redirect, url_for, render_template, request
from werkzeug.security import generate_password_hash


from chains import Chain
app = Flask(__name__)
sf_data = pd.read_csv("sf.csv")
la_data = pd.read_csv("la.csv")

app.config.from_object(Config)

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

# Home Route
@app.route("/")
def home():
    return render_template("home.html")

# Registration Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already registered. Please login or use a different email.', 'error')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

# Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for("page1"))
        flash("Invalid email or password", "danger")
    return render_template("login.html", form=form)

# Logout Route
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

# Crime Data Page
# Crime Data Page
@app.route("/page1")
@login_required
def page1():
    return render_template("page1.html")



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)

