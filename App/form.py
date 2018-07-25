from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    Field1 = StringField('Broker', validators=[DataRequired()])
    Field2 = StringField('Topic', validators=[DataRequired()])
    CheckBox = BooleanField('Check low and high offsets?')
    IntField = IntegerField('Messages to retrieve (default - all)', default=0)
    submit = SubmitField('Submit')
    check_high_low = SubmitField('Check the high and low offsets')
