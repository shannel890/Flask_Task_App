from flask import render_template,redirect,url_for,flash,request
from app import app,db
from app.models import User, Task
from app.forms import Taskform, Userform,Loginform
from flask_login import login_user,login_required,logout_user,current_user
@app.route('/')
def home():
    return render_template('index.html', title='Home')

    
@app.route('/users2',methods=['GET','POST'])

def users2():
    users = User.query.all()

    return render_template('users.html', title='Users',users=users)

@app.route('/tasks',methods=['GET','POST'])
@login_required
def tasks():
    form = Taskform()
    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            completed=form.completed.data,
            user_id=current_user.id
        )
        db.session.add(new_task)
        db.session.commit()
        flash(f'Task {new_task.title} added successfully','success')
        
        return redirect(url_for('tasks'))
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', title='Tasks',form=form,tasks=tasks)
    
    
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
        
        flash(f'Registration for {new_user.first_name} successful','success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', user_form=form)

@app.route('/toggle_task/<int:task_id>',methods=["POST"])
@login_required
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    flash(f'Task {task.title} status update','success')
    return redirect(url_for('tasks'))



@app.route('/delete_task/<int:task_id>', methods=["POST"])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash(f'Task "{task.title}" has been deleted successfully!', 'success')
    return redirect(url_for('tasks'))


@app.route('/delete_user/<int:user_id>', methods=["POST"])
@login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash(f'User  has been deleted successfully!', 'success')
    return redirect(url_for('users'))

  
@app.route('/edit_task/<int:task_id>', methods=['GET','POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    form = Taskform()
    if request.method == 'POST' and form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.completed = form.completed.data
        db.session.commit()
        flash (f'Task {task.title} updated successfully!','success')
        return redirect(url_for('tasks'))
    
    
    elif request.method == 'GET':
        form.title.data = task.title
        form.description.data = task.description
        form.completed.data = task.completed

    tasks = Task.query.all()
    return render_template('tasks.html', title='Edit Tasks', form=form, tasks=tasks, edit_task=True)

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Loginform()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash(f'Welcome Back {user.first_name}', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Failed to login, check your login details and try again', 'danger')

    return render_template('login.html', title='Login', login_form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash(f'Logged out successfully')
    return redirect(url_for('home'))