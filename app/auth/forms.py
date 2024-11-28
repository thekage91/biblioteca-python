from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Accedi')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Accedi')
    