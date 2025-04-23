from flask import render_template,redirect,url_for
from app import app
from app.models import User
from app.forms import Taskform
from app.forms import Userform
from app import db



@app.route('/')
def home():
     users = User.query.all()
     return render_template('index.html', title='Home',users=users)

@app.route('/tasks',methods=['GET','POST'])
def tasks():
    form = Taskform()
    return render_template('tasks.html', title='tasks', form=form)

@app.route('/users',methods=['GET','POST'])
def users():
    form = Userform()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=form.password.data
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', user_form=form)
    
    return render_template('register.html', title='Register', user_form=form)