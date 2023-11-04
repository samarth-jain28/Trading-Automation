from Application import app
from flask import render_template , flash , redirect
from Application.form import LoginForm
from Application.AngleApi import connect 

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


@app.route("/login" , methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = connect(form)
        print(type(data))
        print(data)
        return redirect('/profile')
    return render_template("login.html" , title="Login" ,form=form)

@app.route("/profile"  )
def profile():
    return render_template("profile.html" )