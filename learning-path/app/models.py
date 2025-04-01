from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f"<User {self.username}>"
    
# Database relationships
# 1. One-to-Many relationship A Student can have multiple hobbies
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    hobbies = db.relationship('Hobby', backref='owner', lazy=True)
    
class Hobby(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Post can  have many comments
    comments = db.relationship('Comment', backref="post", lazy=True)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)





"""
One post can have many comments  : One to Many relationship
Post - The parent table
Comment - The child table
"""