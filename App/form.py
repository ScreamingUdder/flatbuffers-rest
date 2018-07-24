from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    Field1 = StringField('Field 1', validators=[DataRequired()])
    Field2 = StringField('Field 2', validators=[DataRequired()])
    CheckBox = BooleanField('Yes/No')
    submit = SubmitField('Sign In')