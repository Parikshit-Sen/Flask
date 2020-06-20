from application import app
from flask_sqlalchemy import SQLAlchemy
from flask import request
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/book'
db=SQLAlchemy(app)
class Login(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    password=db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
@app.route("/login", methods=['GET', 'POST'])
def login():
    if(request.methods=='POST'):
        name=request.form.get('name')
        password=request.form.get('password')
        email=request.form.get('email')
    entry=Login(name=name, password=password,email=email)
    db.session.add(entry)
    db.session.commit()

