from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY']='5162b9a2be630ce47d157e5f7221b3a4043c83842720e36181c91ac9063f266e'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shannel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) 



from app import routes