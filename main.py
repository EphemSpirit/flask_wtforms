from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.secret_key = os.getenv("SECRET_KEY")

class LoginForm(FlaskForm):
    email = EmailField(label='email', validators=[DataRequired(), Email(message="Please enter a valid email address.")])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if request.method == "POST":
        if login_form.validate_on_submit():
            if login_form.email.data == os.getenv("SECRET_EMAIL") and login_form.password.data == os.getenv("SECRET_PASSWORD"):
                return render_template("success.html")
            else:
                return render_template("denied.html")
        else:
            return render_template("login.html")
    else:
        return render_template("login.html", form=login_form)

if __name__ == "__main__":
    app.run(debug=True)