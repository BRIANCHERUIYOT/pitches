from flask import Flask

def create_app(config_name):
# initializing falsk extension
    app= Flask(__name__)
# creating app configuration