from flask import Flask
from flask import render_template
from flask import request,redirect

from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:mishra12@localhost/assig_db'

db = SQLAlchemy(app)

class teacher12(db.Model):
	S_no=db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(80), unique=False, nullable=False)
	HOD = db.Column(db.String(80), unique=False)
	Department = db.Column(db.String(120), unique=False)
	def __repr__(self):
		return "<teacher12: {}>".format(self.S_no,self.Name,self.HOD,self.Department)


class studenttable(db.Model):
	Roll_No=db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(80), unique=False, nullable=False)
	Monitor = db.Column(db.String(80), unique=False)
	Subjects = db.Column(db.String(120), unique=False)
	def __repr__(self):
		return "<studenttable: {}>".format(self.Roll_No,self.Name,self.Monitor,self.Subjects)

@app.route("/students", methods=["GET", "POST"])
def home():
	students=[]
	student = studenttable(Name=request.form.get("Name"),Monitor=request.form.get("Monitor"),Subjects=request.form.get("Subjects"))
	students = studenttable.query.all()
	return render_template("home.html",students=students)

@app.route("/teachers", methods=["GET", "POST"])
def thome():
	teachers=[]
	teacher = teacher12(Name=request.form.get("Name"),HOD=request.form.get("HOD"),Department=request.form.get("Department"))
	teachers = teacher12.query.all()
	return render_template("home2.html",teachers=teachers)

@app.route("/tadd", methods=["GET", "POST"])
def tadd():
	teachers = []
	if request.form:
		teacher = teacher12(Name=request.form.get("Name"),HOD=request.form.get("HOD"),Department=request.form.get("Department"))
		db.session.add(teacher)
		db.session.commit()
		teachers = teacher12.query.all()
	return redirect("/teachers")
@app.route("/add", methods=["GET", "POST"])
def add():
	students = []
	if request.form:
		student = studenttable(Name=request.form.get("Name"),Monitor=request.form.get("Monitor"),Subjects=request.form.get("Subjects"))
		db.session.add(student)
		db.session.commit()
		students = studenttable.query.all()
	return redirect("/students")

@app.route("/update", methods=["GET", "POST"])
def update():
	try:
		if request.method == 'POST':
			data=request.get_json()
			Id=data.get('Roll_No')
			name=data.get('Name')
			monitor=data.get('Monitor')
			sub=data.get('Subjects')
			obj=studenttable.query.filter_by(Roll_No=Id).first()
			obj.Name=name
			obj.Monitor=monitor
			obj.Subjects=sub
			db.session.commit()
			return 'success'
	except:
		return 'Error editing user'

@app.route("/tupdate", methods=["GET", "POST"])
def tupdate():
	try:
		if request.method == 'POST':
			data=request.get_json()
			Id=data.get('s_no')
			name=data.get('Name')
			hod=data.get('HOD')
			dept=data.get('Department')
			obj=teacher12.query.filter_by(S_no=Id).first()
			obj.Name=name
			obj.HOD=hod
			obj.Department=dept
			db.session.commit()
			return 'success'
	except:
		return 'Error editing user'
@app.route("/delete/<int:Roll_No>", methods=["GET", "POST"])
def delete(Roll_No):
	student = studenttable.query.filter_by(Roll_No=Roll_No).delete()
	db.session.commit()
	return redirect("/students")
  
@app.route("/tdelete/<int:S_no>", methods=["GET", "POST"])
def tdelete(S_no):
	teacher = teacher12.query.filter_by(S_no=S_no).delete()
	db.session.commit()
	return redirect("/teachers")
@app.route("/mainpage", methods=["GET", "POST"])
def main():
	
	return render_template("main_page.html")

if __name__ == "__main__":
    app.run(debug=True)