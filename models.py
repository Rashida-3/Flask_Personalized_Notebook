from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(120))
    password=db.Column(db.String(120))
    notes=db.relationship('Note',backref='user',lazy=True)

class Note(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    text=db.Column(db.Text)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))