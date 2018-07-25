from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    Field1 = StringField('Broker', validators=[DataRequired()])
    Field2 = StringField('Topic', validators=[DataRequired()])
    IntField = IntegerField('Messages to retrieve (default - 0 - all)', default=0)
    check_messages = SubmitField('Show messages')
    check_high_low = SubmitField('Check the high and low offsets')
