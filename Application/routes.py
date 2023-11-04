from Application import app
from flask import render_template , flash , redirect
from Application.form import LoginForm
from Application.AngleApi import connect 

@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

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
        if type(data)==str:
            flash('{}'.format(data))
            return redirect('/login') 
        else :
            return render_template('profile.html')
    return render_template("login.html" , title="Login" ,form=form)

