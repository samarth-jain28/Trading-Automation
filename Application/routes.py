from Application import app
from flask import render_template

@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


@app.route("/index")
def index():
    return render_template("base.html")
