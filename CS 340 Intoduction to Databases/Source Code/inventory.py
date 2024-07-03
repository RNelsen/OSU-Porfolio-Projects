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
# This is the backend for the Inventories page

from flask import Flask, render_template, redirect, request, Blueprint
from db import mysql

inventory_page = Blueprint('inventories', __name__)

# Page to add and update medication inventory 
@inventory_page.route('/inventory', methods=["POST", "GET"])
def inventories():
    cur = mysql.connection.cursor()

    # Adding inventory to the database
    if request.method == "POST":
        medication_id = request.form.get('medicationID')
        current_inventory = request.form.get('currentInventory', None)
        min_inventory = request.form.get('minInventory', None)
        max_inventory = request.form.get('maxInventory', None)
        location_shelf = request.form.get('locationShelf', None)
        location_automation = request.form.get('locationAutomation', None) or None
        location_refrigerator = request.form.get('locationInRefrigerator', None) or None

        insert_query = """
        INSERT INTO Inventories (
            medicationID, currentInventory, minInventory, maxInventory, 
            locationShelf, locationAutomation, locationInRefrigerator
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(insert_query, (
            medication_id, current_inventory, min_inventory, max_inventory,
            location_shelf, location_automation, location_refrigerator
        ))
        mysql.connection.commit()

        return redirect('/inventory')

    # Default GET from database to display on page
    cur.execute("""
        SELECT 
            Medications.medicationID,
            Medications.brandName AS 'Brand Name',
            Medications.genericName AS 'Generic Name',
            Medications.strength AS 'Strength',
            Medications.formulation AS 'Formulation',
            Inventories.currentInventory AS 'Current Inventory',
            Inventories.minInventory AS 'Min. Inventory',
            Inventories.maxInventory AS 'Max. Inventory',
            Inventories.locationShelf AS 'Location on shelf',
            Automations.automationName AS 'Location in Automation',
            Refrigerators.refrigeratorName AS 'Location in Refrigerator'
        FROM Inventories
        JOIN Medications ON Inventories.medicationID = Medications.medicationID
        LEFT JOIN Automations ON Inventories.locationAutomation = Automations.automationID
        LEFT JOIN Refrigerators ON Inventories.locationInRefrigerator = Refrigerators.refrigeratorID
    """)
    inventory_data = cur.fetchall()

    cur.execute("""
        SELECT medicationID, brandName, strength, formulation 
        FROM Medications
    """)
    medications = cur.fetchall()

    # Get location in automations from database
    cur.execute("SELECT automationID, automationName FROM Automations")
    automations = cur.fetchall()

    # Get locations in refrigerators from database
    cur.execute("SELECT refrigeratorID, refrigeratorName FROM Refrigerators")
    refrigerators = cur.fetchall()
    
    cur.close()
    
    return render_template(
        "inventory.html", 
        inventory_data=inventory_data, 
        medications=medications, 
        automations=automations, 
        refrigerators=refrigerators
    )
