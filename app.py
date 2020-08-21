from  flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
file_path = os.path.abspath(os.getcwd())+"/blog.db"

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path



db = SQLAlchemy(app)

class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()
    return render_template('post.html',post=post)
@app.route('/contact')
def contact():
   return render_template('contact.html')

@app.route('/test')
def test():
   return render_template('test.html')   
@app.route('/addblog',methods=['GET','POST'])
def addblog():
    if request.method=="POST":
        title = request.form['title']
        subtitle = request.form['subtitle']
        author = request.form['author']
        content = request.form['content']
        post = Blogpost(title=title,subtitle=subtitle,author=author,content=content,date_posted = datetime.now())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
   

@app.route('/add')
def add():
   return render_template('add.html')   

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)