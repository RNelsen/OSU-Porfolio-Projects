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
# This is the backend for the customers page


from flask import Flask, render_template, redirect, request, Blueprint
from db import mysql

customers_page = Blueprint('customers', __name__)

# Function to display Customers from the database
@customers_page.route('/customers',  methods=["POST", "GET"])
def customers():

    # Default GET from database to display on page
    if request.method == "GET":
        cur = mysql.connection.cursor()
        query = '''SELECT customerID, firstName, lastName, email, phoneNumber FROM Customers'''
        cur.execute(query)
        customers_data = cur.fetchall()
        cur.close()
        return render_template("customers.html", customers_data=customers_data)

# Function to Display which customer to edit
@customers_page.route('/edit_customer/<int:customer_id>', methods=["GET"])
def edit_customer(customer_id):
    cur = mysql.connection.cursor()
    query = '''SELECT * FROM Customers WHERE customerID = %s'''
    cur.execute(query, (customer_id,))
    customer_data = cur.fetchone()
    cur.close()
    if customer_data:
        return render_template("edit_customer.html", customer=customer_data)
    else:
        return 'Customer not found', 404

# Function to update the customer after editing
@customers_page.route('/update_customer/<int:customer_id>', methods=["POST"])
def update_customer(customer_id):

    # Extract form data
    first_name = request.form.get("firstName")
    last_name = request.form.get("lastName")
    email = request.form.get("email")
    phone_number = request.form.get("phoneNumber")

    # If email or phone number fields are empty, set them to 'None' or any other placeholder
    # Date: 11/20/23
    # The method for checking and replacing empty strings was adapted from a Stack Overflow post:
    # "Stripping a character only once in Python" Source URL: https://stackoverflow.com/questions/47160355
    email = email if email.strip() != '' else 'None'
    phone_number = phone_number if phone_number.strip() != '' else 'None'

    cur = mysql.connection.cursor()
    update_query = '''
        UPDATE Customers
        SET firstName = %s, lastName = %s, email = %s, phoneNumber = %s
        WHERE customerID = %s
    '''
    cur.execute(update_query, (first_name, last_name, email, phone_number, customer_id))
    mysql.connection.commit()
    cur.close()
    
    return redirect('/customers')

# Function to Add customer to the database
@customers_page.route('/add_customer', methods=["POST"])
def add_customer():

    # Extract form data
    if request.method == "POST":
        first_name = request.form["firstName"]
        last_name = request.form["lastName"]
        email = request.form["email"] or None
        phone_number = request.form["phoneNumber"] or None
        
        cur = mysql.connection.cursor()
        query = '''INSERT INTO Customers (firstName, lastName, email, phoneNumber)
                   VALUES (%s, %s, %s, %s)'''
        cur.execute(query, (first_name, last_name, email, phone_number))
        mysql.connection.commit()
        cur.close()
        return redirect("/customers")
    
