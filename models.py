from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(9), unique = True, nullable = False)
    firstName = db.Column(db.String(80), nullable = False)
    lastName = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(12), unique=True)
    course_id = db.Column(db.String(3), db.ForeignKey('course.id'))
    course = db.relationship('Course', 
        backref=db.backref('students',lazy='dynamic'))

    def __init__(self, uid, firstName, lastName, course, phone=None):
        self.uid = uid
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
        self.course = course


class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dateAdded = db.Column(db.DateTime)

    student_id = db.Column(db.String, db.ForeignKey('student.id'))
    student = db.relationship('Student',
        backref=db.backref('points', lazy='dynamic'))
    pointType = db.Column(db.Enum('participation','bonus'), nullable = False)
    
    def __init__(self, student, dateAdded, pointType):
        self.student = student
        self.dateAdded = dateAdded   
        self.pointType = pointType


class Course(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String (10), nullable = False)
    quarter = db.Column(db.String(3), nullable=False)
    
    def __init__(self, name, quarter):
        self.name = name
        self.quarter = quarter

