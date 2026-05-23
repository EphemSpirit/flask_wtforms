from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField
from dotenv import load_dotenv
import os

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.secret_key = os.getenv("SECRET_KEY")

class LoginForm(FlaskForm):
    email = StringField('email')
    password = StringField('password')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html", form=LoginForm())

if __name__ == "__main__":
    app.run(debug=True)