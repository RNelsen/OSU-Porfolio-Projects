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
# This is the backend for the refrigerators page


from flask import Flask, render_template, redirect, request, Blueprint
from db import mysql

fridge_page = Blueprint('fridge', __name__)

# Function to display and add refrigerators to the database
@fridge_page.route('/refrigerators',  methods=["POST", "GET"])
def fridge():

    # Default GET from database to display on page
    if request.method == "GET":
        query = '''SELECT refrigeratorId AS "Refrigerator ID", 
                   refrigeratorName AS "Refrigerator Name"
                   FROM Refrigerators;  '''
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("refrigerators.html", data=data)
    
    # If adding refrigerator then do this.
    if request.method == "POST":

        if request.form.get("Add_Refrigerator"):
            fridgeName = request.form["addRefrigerator"]

        if fridgeName == "":
            pass
        else:
            query = '''INSERT INTO Refrigerators (refrigeratorName) VALUES (%s)'''
            cur = mysql.connection.cursor()
            cur.execute(query, (fridgeName,))
            mysql.connection.commit()
        
        return redirect('/refrigerators')