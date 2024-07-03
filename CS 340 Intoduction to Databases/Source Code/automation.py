# Daniel Reid Nelsen and Jennifer Pribbeno
# Project Group 47
# CS 340 Introduction to Databases
# Portfolio Project
# Due: 12/11/2023
# Description:  Project demonstrating setting up database in MySQL.  Then 
#               Implementing a web application to interact and manlipulate 
#               the database. Descriptions of the project can be found in 
#               the index.html file under the template folder.  
#               Web app is programmed with Python/Flask.
# 
# This is the backend for the automations page

from flask import Flask, render_template, redirect, request, Blueprint
from db import mysql


automation_page = Blueprint('automation', __name__)

@automation_page.route('/automation',  methods=["GET", "POST"])
def automation():


    # Default GET from database to display on page
    if request.method == "GET":
        query = '''SELECT automationID AS "Automation ID", 
                automationName AS "Automation Name"
                FROM Automations;  '''
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("automation.html", data=data)
    
    # Adding an automation system to the database
    if request.method == "POST":

        if request.form.get("Add_Automation"):
            autoName = request.form["addAutomation"]

        # Name is required so not adding if blank
        if autoName == "":
            pass
        else:
            query = '''INSERT INTO Automations (automationName) VALUES (%s)'''
            cur = mysql.connection.cursor()
            cur.execute(query, (autoName,))
            mysql.connection.commit()
        
        return redirect('/automation')