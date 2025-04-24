from flask import render_template,redirect,url_for,flash
from app import app,db
from app.models import User, Task
from app.forms import Taskform, Userform
@app.route('/')
def home():
    return render_template('index.html', title='Home',users=users)

    
@app.route('/users2',methods=['GET','POST'])
def users2():
    users = User.query.all()

    return render_template('users.html', title='Users',users=users)

@app.route('/tasks',methods=['GET','POST'])
def tasks():
    form = Taskform()
    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            completed=form.completed.data,
            user_id=1
        )
        db.session.add(new_task)
        db.session.commit()
        flash(f'Task {new_task.title} added successfully','success')
        
        return redirect(url_for('tasks'))
    tasks = Task.query.all()
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
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    flash(f'Task {task.title} status update','success')
    return redirect(url_for('tasks'))



@app.route('/delete_task/<int:task_id>', methods=["POST"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash(f'Task "{task.title}" has been deleted successfully!', 'success')
    return redirect(url_for('tasks'))

@app.route('/delete_user/<int:user_id>', methods=["POST"])
def delete_user2(user_id):
    task = Task.query.get_or_404(user_id)
    db.session.delete(users2)
    db.session.commit()
    flash(f'User  has been deleted successfully!', 'success')
    return redirect(url_for('users'))
  