from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , BooleanField , SubmitField
from wtforms import validators

class LoginForm(FlaskForm):
    username = StringField('Client Id' , [ validators.DataRequired(),validators.length(min=5 , max=8) ], render_kw={"placeholder":"CLIENT ID" })
    pin = PasswordField('Pin' , [validators.DataRequired(),validators.length(min=4,max=4)] , render_kw={"placeholder ":"PIN" })
    totp = StringField('Totp' , [validators.DataRequired()] , render_kw={"placeholder":"TOTP"})
    submit = SubmitField('Login' )
