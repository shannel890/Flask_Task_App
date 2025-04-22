from app import db

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    task = db.relationship('Task', backref='user', lazy=True)

    def __repr__(self):
          return f' {self.first_name} {self.last_name}'


    def display_user(self):
        return f"User ID: {self.id}, Username: {self.username}, Name: {self.first_name} {self.last_name}"

    def display_tasks(self):
        if not self.task:
            return f"{self.username} has no tasks."
        return "\n".join([task.display_task() for task in self.task])

class Task(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    title = db.Column(db.String(20), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

def display_task(self):
    status = "Completed" if self.completed else "Pending"
    return f"Task ID: {self.id}, Title: {self.title}, Status: {status}, Description: {self.description}"





