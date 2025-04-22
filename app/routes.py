from flask import render_template
from app import app
from app.models import User



@app.route('/')
def home():
     return render_template('index.html',title='Home')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html',title='tasks')

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html',title='users',users=users)