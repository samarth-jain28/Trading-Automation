from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , BooleanField , SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Client Id' , validators = [DataRequired()])
    pin = PasswordField('Pin' , validators = [DataRequired()])
    submit = SubmitField('Login' )