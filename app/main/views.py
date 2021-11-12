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
     
     
     
     
     return render_template('index.html',)
 
