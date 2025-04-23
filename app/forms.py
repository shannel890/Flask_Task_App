from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,BooleanField,SubmitField,PasswordField
from wtforms.validators import DataRequired
class Taskform(FlaskForm):
    title = StringField('Task Title')
    description = TextAreaField('Task Description')
    completed = BooleanField('Completed')
    submit = SubmitField('Register')


class Userform(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    first_name = StringField('Firstname',validators=[DataRequired()])
    last_name = StringField('Lastname',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Register',validators=[DataRequired()])