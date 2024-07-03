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
# This is the backend for Wholesalers page


from flask import Flask, render_template, redirect, request, Blueprint
from db import mysql


wholesalers_page = Blueprint('wholesalers', __name__)

# Function to display wholesalers
@wholesalers_page.route('/wholesalers',  methods=["GET"])
def wholesalers():
    if request.method == "GET":
        cur = mysql.connection.cursor()
        query = '''SELECT wholesalerID, wholesalerName, contactName, contactEmail, contactPhoneNumber, address FROM Wholesalers'''
        cur.execute(query)
        wholesaler_data = cur.fetchall()
        cur.close()
        return render_template("wholesalers.html", wholesaler_data=wholesaler_data)

# Function to add wholesaler
@wholesalers_page.route('/add_wholesaler', methods=["POST"])
def add_wholesaler():
    if request.method == "POST":
        wholesaler_name = request.form.get("wholesalerName")
        contact_name = request.form.get("contactName", None)  # Default to None if not provided
        contact_email = request.form.get("contactEmail", None)
        contact_phone_number = request.form.get("contactPhoneNumber", None)
        address = request.form.get("address", None)

        cur = mysql.connection.cursor()
        query = '''INSERT INTO Wholesalers (wholesalerName, contactName, contactEmail, contactPhoneNumber, address) VALUES (%s, %s, %s, %s, %s)'''
        cur.execute(query, (wholesaler_name, contact_name, contact_email, contact_phone_number, address))
        mysql.connection.commit()
        cur.close()

        return redirect("/wholesalers")
    
# Function to display and edit wholesaler data
@wholesalers_page.route('/edit_wholesaler/<int:wholesalerID>', methods=["POST", "GET"])
def edit_wholesaler(wholesalerID):
    cur = mysql.connection.cursor()

    # Display wholesaler to edit
    if request.method == "GET":
        query = '''SELECT * FROM Wholesalers WHERE wholesalerID = %s'''
        cur.execute(query, [wholesalerID])
        wholesaler_data = cur.fetchone()
        cur.close()
        return render_template('edit_wholesaler.html', wholesaler=wholesaler_data)

    # Update the wholesaler after editing
    if request.method == "POST":
        # Extract form data
        wholesaler_name = request.form["wholesalerName"]
        contact_name = request.form.get("contactName")
        contact_email = request.form.get("contactEmail")
        contact_phone_number = request.form.get("contactPhoneNumber")
        address = request.form.get("address")

        # Update wholesaler data
        update_query = '''UPDATE Wholesalers SET 
                          wholesalerName = %s, 
                          contactName = %s, 
                          contactEmail = %s, 
                          contactPhoneNumber = %s,
                          address = %s
                          WHERE wholesalerID = %s'''
        cur.execute(update_query, (wholesaler_name, contact_name, contact_email, contact_phone_number, address, wholesalerID))
        mysql.connection.commit()
        cur.close()

        return redirect('/wholesalers')