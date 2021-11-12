from flask import render_template
from . import main 
from models import Pitches,User

@main.route('/')
def index():
     """
     view route page function
     """
     pitches= Pitches.query.all()
     users =User.query.all()
     religion = Pitches.query.filter_by(category= 'religion').all()
     food = Pitches.query.filter_by(category= 'food').all()      
     sports = Pitches.query.filter_by(category= 'sports').all()  
     music = Pitches.query.filter_by(category= 'music').all()  
     
     
     return render_template('index.html',pitches=pitches, users=users,religion=religion,food=food,sports=sports,music=music)
 
