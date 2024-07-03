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
# This is the backend for the Purchases page

from flask import Flask, render_template, redirect, request, Blueprint
from db import mysql

purchases_page = Blueprint('purchases', __name__)

# Function to add and view purchases.  This is an intersection table with 
# Customers and Medications
@purchases_page.route('/purchases', methods=["POST", "GET"])
def purchases():
    cur = mysql.connection.cursor()

    # adding a new purchase
    if request.method == "POST":
        medication_id = request.form.get('medicationId')
        customer_id = request.form.get('customerId')
        date_of_purchase = request.form.get('dateOfPurchase')
        
        insert_query = '''
        INSERT INTO Purchases (medicationID, customerID, dateOfPurchase)
        VALUES (%s, %s, %s)
        '''
        cur.execute(insert_query, (medication_id, customer_id, date_of_purchase))
        mysql.connection.commit()
        return redirect("/purchases")
    
    # retrieving the purchases page
    else:
        purchases_query = '''
        SELECT Purchases.purchaseID AS "Purchase ID", 
            Medications.medicationID AS "Medication ID", 
            Medications.brandName AS "Brand Name", 
            Medications.genericName AS "Generic Name", 
            CONCAT(Customers.customerID, ' - ', Customers.lastName, ', ', Customers.firstName) AS "Customer",
            Purchases.dateOfPurchase AS "Date of Purchase"
        FROM Purchases
        JOIN Medications ON Purchases.medicationID = Medications.medicationID
        JOIN Customers ON Purchases.customerID = Customers.customerID
        ORDER BY purchaseID ASC;
        '''
        cur.execute(purchases_query)
        purchases_data = cur.fetchall()

        # Get medications for dropdown
        medications_query = '''
        SELECT medicationID, brandName, strength, formulation
        FROM Medications;
        '''
        cur.execute(medications_query)
        medications_data = cur.fetchall()

        # Get customers for dropdown
        customers_query = '''
        SELECT customerID, CONCAT(customerID, ' - ', lastName, ', ', firstName) AS customerDisplay
        FROM Customers;
        '''
        cur.execute(customers_query)
        customers_data = cur.fetchall()

        cur.close()
        return render_template("purchases.html", purchases_data=purchases_data, medications_data=medications_data, customers_data=customers_data)

# Function to Delete a purchase from database
@purchases_page.route('/delete_purchase/<int:id>')
def delete_purchase(id):
    cur = mysql.connection.cursor()
    query = "DELETE FROM Purchases WHERE purchaseID = %s;"
    cur.execute(query, (id,))
    mysql.connection.commit()
    cur.close()
    return redirect("/purchases")

# Function to populate the edit_purchase.html page
@purchases_page.route('/edit_purchase/<int:purchaseID>', methods=["POST", "GET"])
def edit_purchase(purchaseID):
    cur = mysql.connection.cursor()

    # Default GET from database to display on page
    if request.method == "GET":
        query = "SELECT * FROM Purchases WHERE purchaseID = '%s';"
        cur.execute(query, [purchaseID])
        purchase_data = cur.fetchone()

        medication_query = '''
        SELECT medicationID, brandName, genericName from Medications'''
        cur.execute(medication_query)
        medication_data = cur.fetchall()
        
        customer_query = '''
        SELECT customerID, firstName, lastName from Customers'''
        cur.execute(customer_query)
        customer_data = cur.fetchall()

        cur.close()

        return render_template('edit_purchase.html', purchase=purchase_data, medications=medication_data, customers=customer_data)

    # Updating the purchase
    if request.method == "POST":

        # Extract form data
        if request.form.get("Update_Purchase"):
            customerID = request.form["customerID"]
            medicationID = request.form["medicationID"]
            lastPurchased = request.form["lastPurchased"]

            update_query = '''
                    Update Purchases SET
                    customerID = %s, medicationID = %s,
                    dateOfPurchase = %s
                    WHERE purchaseID = %s'''
            cur.execute(update_query, (customerID, medicationID, lastPurchased, purchaseID))
            mysql.connection.commit()
            cur.close()

            return redirect("/purchases")
    