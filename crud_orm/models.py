from flask import Flask
from flask import render_template
from flask import request,redirect

from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:mishra12@localhost/assig_db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False 
db = SQLAlchemy(app)



class student12(db.Model):
	Roll_No=db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(80), unique=False, nullable=False)
	Monitor = db.Column(db.String(80), unique=False)
	Subjects = db.Column(db.String(120), unique=False)
	def __repr__(self):
		return "<student12: {}>".format(self.Roll_No,self.Name,self.Monitor,self.Subjects)
