# Daniel Reid Nelsen and Jennifer Pribbeno
# Project Group 47
# CS 340 Introduction to Databases
# Portfolio Project
# Due: 12/11/2023
# Description:  Project demonstrating setting up database in MySQL.  Then 
#               Implementing a web application to interact and manlipulate 
#               the database.  This is the main file for said project.  Description
#               of the project can be found in the index.html file under the 
#               template folder.  Web app is programmed with Python/Flask.


from flask import Flask, render_template, redirect, request, Blueprint
import os

# Date: 11/29/2023
# This project is based on the tutorial and code structure provided by the OSU CS340 eCampus Flask Starter App.
# Original repository: https://github.com/osu-cs340-ecampus/flask-starter-app
# Forked from: https://github.com/gkochera/CS340-demo-flask-app

# Source for splitting pages into multiple .py files
# Split Python Flask app into multiple files
# https://stackoverflow.com/questions/15231359/split-python-flask-app-into-multiple-files
# Accessed: 11/4/2023

from drugs import drugs_page
from automation import automation_page
from purchases import purchases_page
from fridge import fridge_page
from customers import customers_page
from inventory import inventory_page
from wholesalers import wholesalers_page
from db import mysql

# Configuration

app = Flask(__name__)
app.register_blueprint(drugs_page)
app.register_blueprint(automation_page)
app.register_blueprint(purchases_page)
app.register_blueprint(fridge_page)
app.register_blueprint(customers_page)
app.register_blueprint(inventory_page)
app.register_blueprint(wholesalers_page)

# database connection info
app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
app.config["MYSQL_USER"] = ""
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = ""
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql.init_app(app)

# Default Routes 

@app.route('/')
def home():
    return render_template("index.html")

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 32346)) 
    
    app.run(host='0.0.0.0',port=port, debug=True) 