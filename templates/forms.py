from flask_wtf import FlaskForm
from flask_wtf

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[])