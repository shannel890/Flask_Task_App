from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Task page."

@app.route('/tasks')
def tasks():
    return "<h1>This is the task list page.</h1>"

@app.route('/about')
def about():
    return "<h1>This page is dedicated on about!</h1>""<h3>This  page will help us now more about the progect on flask and its features encouraging us to be more resilient and hardworking.</h3>"



if __name__ == '__main__':
    app.run(debug=True)
