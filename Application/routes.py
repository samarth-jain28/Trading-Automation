from Application import app
from flask import render_template

@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


@app.route("/index")
def index():
    return render_template("base.html" , title="HomePage")

@app.route("/about")
def about():
    return render_template("about.html" , title="About Us")

@app.route("/login")
def login():
    return render_template("login.html" , title="Login")