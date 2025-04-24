from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,BooleanField,SubmitField,PasswordField
from wtforms.validators import DataRequired
class Taskform(FlaskForm):
    title = StringField('Task Title', validators=[DataRequired()])
    description = TextAreaField('Task Description', validators=[DataRequired()])
    completed = BooleanField('Completed')
    submit = SubmitField('Submit')


class Userform(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    first_name = StringField('Firstname',validators=[DataRequired()])
    last_name = StringField('Lastname',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Register',validators=[DataRequired()])