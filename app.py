from flask import Flask, render_template, request
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

class alphaDB(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String, nullable=False)
    writer = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    hit = db.Column(db.String, nullable=False)
    req = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()

@app.route("/database/create/")
def database_create():
    number_receive = request.args.get("number")
    subject_receive = request.args.get("subject")
    writer_receive = request.args.get("writer")
    date_receive = request.args.get("date")
    hit_receive = request.args.get("hit")
    req_receive = request.args.get("req")

    database = alphaDB(number=number_receive, subject=subject_receive, writer=writer_receive, date=date_receive, hit=hit_receive, req=req_receive)
    db.session.add(database)
    db.session.commit()
    return render_template('index_mainpage.html')

app.run(debug=True)