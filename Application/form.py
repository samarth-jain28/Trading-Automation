from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , BooleanField , SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Client Id' , validators = [DataRequired()] , render_kw={"placeholder":"CLIENT ID" })
    pin = PasswordField('Pin' , validators = [DataRequired()] , render_kw={"placeholder ":"PIN" })
    totp = StringField('Totp' , validators = [DataRequired()] , render_kw={"placeholder":"TOTP"})
    submit = SubmitField('Login' )
