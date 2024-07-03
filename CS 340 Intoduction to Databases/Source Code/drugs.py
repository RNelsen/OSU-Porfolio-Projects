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
# This is the backend for the medications page

from flask import Flask, render_template, redirect, flash, request, Blueprint
from db import mysql


drugs_page = Blueprint('drugs', __name__)

# Function to display and add new medications to the database
@drugs_page.route('/drugs', methods=["POST", "GET"])
def drugs():

    # if we are adding new medication do this.
    if request.method == "POST":

        if request.form.get("Add_Med"):

            brandName = request.form["brandName"]
            genericName = request.form["genericName"]
            strength = request.form["strength"]
            formulation = request.form["formulation"]
            ndcNumber = request.form["ndcNumber"]
            upcNumber = request.form["upcNumber"]
            wholesaler = None if request.form["wholesaler"] == "0" else request.form["wholesaler"]
            cost = request.form["cost"]
            bottleSize = request.form["bottleSize"]
            date = request.form["dateOfPurchase"]

            # This conditional is so that page is able to handle NULL wholesalers values
            if wholesaler == "":
                query = '''INSERT INTO Medications (brandName, genericName, strength, 
                        formulation, upcNumber, ndcNumber, costToBuy, bottleCountSize, lastPurchased)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
                cur = mysql.connection.cursor()
                cur.execute(query, (brandName, genericName, strength, 
                                    formulation, upcNumber, ndcNumber, cost, bottleSize, date))
                mysql.connection.commit()
            else:
                query = '''INSERT INTO Medications (brandName, genericName, strength, 
                    formulation, upcNumber, ndcNumber, costToBuy, bottleCountSize, wholesalerID, lastPurchased)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
                cur = mysql.connection.cursor()
                cur.execute(query, (brandName, genericName, strength, 
                                    formulation, upcNumber, ndcNumber, cost, bottleSize, wholesaler, date))
                mysql.connection.commit()
            
            return redirect("/drugs")

    # if page is just going to display medication do this.
    if request.method == "GET":
        query = '''SELECT Medications.medicationID AS "Medication ID", 
                    Medications.brandName AS "Brand Name", 
                    Medications.genericName AS "Generic Name", 
                    Medications.strength AS "Strength", 
                    Medications.formulation AS "Formulation", 
                    Medications.upcNumber AS "UPC Number", 
                    Medications.ndcNumber AS "NDC Number", 
                    Medications.costToBuy AS "Cost to Buy", 
                    Medications.bottleCountSize AS "Bottle Count Size", 
                    Wholesalers.wholesalerName AS "Wholesaler", 
                    Medications.lastPurchased AS "Last Purchased Date"
                    FROM Medications
                    LEFT JOIN Wholesalers ON Medications.wholesalerID = Wholesalers.wholesalerID'''
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        wholesalerQueury = '''Select wholesalerID, wholesalerName from Wholesalers;'''
        wholesalerNames = mysql.connect.cursor()
        wholesalerNames.execute(wholesalerQueury)
        wholesalerData = wholesalerNames.fetchall()

        return render_template("drugs.html", data=data, wholesalerData=wholesalerData)

# Function to edit medications
@drugs_page.route('/edit_medication/<int:medicationID>', methods=["POST", "GET"])
def edit_medication(medicationID):
    cur = mysql.connection.cursor()

    # Handling GET request - Fetch and display current medication data
    if request.method == "GET":
        query = '''SELECT * FROM Medications WHERE medicationID = %s'''
        cur.execute(query, [medicationID])
        medication_data = cur.fetchone()

        wholesalerQuery = '''SELECT wholesalerID, wholesalerName FROM Wholesalers;'''
        cur.execute(wholesalerQuery)
        wholesalerData = cur.fetchall()
        cur.close()

        return render_template('edit_medication.html', medication=medication_data, wholesalerData=wholesalerData)

    # Handling POST request - Update medication data
    if request.method == "POST":

        # Extract form data
        if request.form.get("Update_Med"):
            brandName = request.form["brandName"]
            genericName = request.form["genericName"]
            strength = request.form["strength"]
            formulation = request.form["formulation"]
            ndcNumber = request.form["ndcNumber"]
            upcNumber = request.form["upcNumber"]
            wholesalerID = None if request.form["wholesaler"] == "0" else request.form["wholesaler"]
            cost = request.form["costToBuy"]
            bottleSize = request.form["bottleCountSize"]
            lastPurchasedDate = request.form["lastPurchased"]

            # If wholesalerID is empty, assume NULL
            if not wholesalerID:
                update_query = '''UPDATE Medications SET 
                                  brandName = %s, genericName = %s, strength = %s, 
                                  formulation = %s, ndcNumber = %s, upcNumber = %s, 
                                  costToBuy = %s, bottleCountSize = %s, 
                                  lastPurchased = %s, wholesalerID = NULL
                                  WHERE medicationID = %s'''
                cur.execute(update_query, (brandName, genericName, strength, 
                                           formulation, ndcNumber, upcNumber, 
                                           cost, bottleSize, lastPurchasedDate, medicationID))
            else:
                update_query = '''UPDATE Medications SET 
                                  brandName = %s, genericName = %s, strength = %s, 
                                  formulation = %s, ndcNumber = %s, upcNumber = %s, 
                                  costToBuy = %s, bottleCountSize = %s, 
                                  lastPurchased = %s, wholesalerID = %s
                                  WHERE medicationID = %s'''
                cur.execute(update_query, (brandName, genericName, strength, 
                                           formulation, ndcNumber, upcNumber, 
                                           cost, bottleSize, lastPurchasedDate, wholesalerID, medicationID))
                
        mysql.connection.commit()
        cur.close()

        return redirect('/drugs')

# Function to delete medication from database
@drugs_page.route('/delete_med/<int:id>')
def delete_med(id):
    query = "DELETE from Medications WHERE medicationID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()
    return redirect("/drugs")