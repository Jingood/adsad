from flask import Flask, render_template, request, redirect, url_for,jsonify
import os
from flask_sqlalchemy import SQLAlchemy



basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),nullable=False)
    date = db.Column(db.String(20),nullable=False)
    title = db.Column(db.String(50),nullable=False)
    content = db.Column(db.Text,nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')


# 게시물 추가
@app.route('/post_add')
def post_add():
    return render_template('post_add.html')


@app.route('/post_add_button',methods=['GET','POST'])
def post_add_button():
    username_receive = request.args.get("username")
    date_receive = request.args.get("date")
    title_receive = request.args.get("title")
    content_receive = request.args.get("content")
    
    post = Post(username = username_receive, date= date_receive, title= title_receive, content= content_receive)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('post_filter'))

@app.route('/post')
def post_filter():
    post = Post.query.all()
    return render_template('post.html', data=post)


# if __name__ == '__main__':  
app.run(debug=True)


"""
강민준(AI튜터)flask를 통해 db 조회하는 방법
강민준(AI튜터)flask 로 db 연동, 초기화, 조회
강민준(AI튜터)reoute() 함수 사용방법
강민준(AI튜터)flask 자체를 study 하게 되실겁니다
"""