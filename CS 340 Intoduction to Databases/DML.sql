-- Daniel Reid Nelsen and Jennifer Pribbeno
-- Project Group 47
-- CS 340 Introduction to Databases
-- Portfolio Project
-- Due: 12/11/2023
-- Description:  Project demonstrating setting up database in MySQL.  Then 
--               Implementing a web application to interact and manlipulate 
--               the database. Descriptions of the project can be found in 
--               the index.html file under the template folder.  
--               Web app is programmed with Python/Flask.

-- This file holds sample queries made when interacting with the database
-- These queries can be found in the .py files for the project.
-- Inputted values are denoted with a ":".  For exampele, SET brandName = :brandNameInput

-- Medications (Drug) Page
-- get all Medications
SELECT Medications.medicationID AS "Medication ID", 
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
LEFT JOIN Wholesalers ON Medications.wholesalerID = Wholesalers.wholesalerID;

-- get wholesalers on Medications page
Select wholesalerID, wholesalerName from Wholesalers;

-- Get Medication that is to be edited.
SELECT * FROM Medications WHERE medicationID = :medicationID

-- add a new Medication when Wholesaler is NULL
INSERT INTO Medications (brandName, genericName, strength, formulation, upcNumber, ndcNumber, costToBuy, bottleCountSize, wholesalerID, lastPurchased)
VALUES ('Brand Name', 'Generic Name', 'Strength', 'Formulation', 'UPC', 'NDC', Cost, 'BottleSize', 'Date');

-- add a new Medication when Wholesaler has a value
INSERT INTO Medications (brandName, genericName, strength, formulation, upcNumber, ndcNumber, costToBuy, bottleCountSize, wholesalerID, lastPurchased)
VALUES ('Brand Name', 'Generic Name', 'Strength', 'Formulation', 'UPC', 'NDC', Cost, 'BottleSize', 'Wholesaler', 'Date');

-- update a Medication with Wholesaler
UPDATE Medications
SET brandName = :brandNameInput, 
    genericName = :genericNameInput, 
    strength = :strengthInput, 
    formulation = :formulationInput, 
    upcNumber = :upcNumberInput, 
    ndcNumber = :ndcNumberInput, 
    costToBuy = :costToBuyInput, 
    bottleCountSize = :bottleCountSizeInput, 
    wholesalerID = :wholesalerID
    lastPurchased = :lastPurchasedInput 
WHERE medicationID = :medicationIDInput;

-- update a Medication without Wholesaler
UPDATE Medications
SET brandName = :brandNameInput, 
    genericName = :genericNameInput, 
    strength = :strengthInput, 
    formulation = :formulationInput, 
    upcNumber = :upcNumberInput, 
    ndcNumber = :ndcNumberInput, 
    costToBuy = :costToBuyInput, 
    bottleCountSize = :bottleCountSizeInput, 
    wholesalerID = NULL
    lastPurchased = :lastPurchasedInput 
WHERE medicationID = :medicationIDInput;

-- delete a Medication
DELETE from Medications WHERE medicationID = :medicationIDSelectedFromMedicationsPage;

-- Wholesalers Page
-- get all Wholesalers
SELECT wholesalerID AS "Wholesaler ID", 
       wholesalerName AS "Wholesaler Name", 
       contactName AS "Contact Name", 
       address AS "Address", 
       phone AS "Phone Number", 
       email AS "Email"
FROM Wholesalers;

-- Select Wholesaler
SELECT * FROM Wholesalers WHERE wholesalerID = :wholesalerID

-- add Wholesaler
INSERT INTO Wholesalers (wholesalerName, contactName, address, phone, email) 
VALUES (:wholesalerNameInput, :contactNameInput, :addressInput, :phoneInput, :emailInput);

-- update Wholesaler
UPDATE Wholesalers
SET wholesalerName = :wholesalerNameInput, 
    contactName = :contactNameInput, 
    address = :addressInput, 
    phone = :phoneInput, 
    email = :emailInput
WHERE wholesalerID = :wholesalerIDInput;

-- delete Wholesaler
DELETE FROM Wholesalers WHERE wholesalerID = :wholesalerIDSelectedFromWholesalersPage;


-- Automations Page
-- get all Automations
SELECT automationID AS "Automation ID", automationName AS "Automation Name"
FROM Automations;

-- add Automation
INSERT INTO Automations (automationName)
VALUES (:automationNameInput);


-- Refrigerators Page
-- get all Refrigerators
SELECT refrigeratorId AS "Refrigerator ID", refrigeratorName AS "Refrigerator Name"
FROM Refrigerators;

-- add Refrigerator
INSERT INTO Refrigerators (refrigeratorName)
VALUES (:refrigeratorNameInput);


-- Inventories Page
-- get all Inventories
SELECT Medications.brandName AS 'Brand Name',
    Medications.genericName AS 'Generic Name',
    Inventories.currentInventory AS 'Current Inventory',
    Inventories.minInventory AS 'Min. Inventory',
    Inventories.maxInventory AS 'Max. Inventory',
    Inventories.locationShelf AS 'Location on shelf',
    Automations.automationName AS 'Location in Automation',
    Refrigerators.refrigeratorName AS 'Location in Refrigerator'
FROM Inventories
JOIN Medications ON Inventories.medicationID = Medications.medicationID
LEFT JOIN Automations ON Inventories.automationID = Automations.automationID
LEFT JOIN Refrigerators ON Inventories.locationInRefrigerator = Refrigerators.refrigeratorID;

-- get all medication data for use on Inventories page
SELECT medicationID, brandName, strength, formulation FROM Medications;

-- get location from Automations table for use on Inventories page
SELECT automationID, automationName FROM Automations;

-- get location in Refrigerators table for use on Inventories page
SELECT refrigeratorID, refrigeratorName FROM Refrigerators

-- add Inventory
INSERT INTO Inventories (medicationID, currentInventory, minInventory, maxInventory, locationShelf, locationBox, locationAutomation, locationInRefrigerator)
VALUES (:medicationIDInput, :currentInventoryInput, :minInventoryInput, :maxInventoryInput, :locationShelfInput, :locationBoxOnShelfInput, :locationAutomationInput, :locationRefrigeratorInput);


-- Purchases Page
-- get all Purchases
SELECT Purchases.purchaseID AS "Purchase ID", 
       Medications.brandName AS "Medication Name", 
       Customers.firstName AS "Customer First Name", 
       Customers.lastName AS "Customer Last Name", 
       Purchases.dateOfPurchase AS "Date of Purchase" 
FROM Purchases
JOIN Medications ON Purchases.Medications_medicationID = Medications.medicationID 
JOIN Customers ON Purchases.Customers_customerID = Customers.customerID        
ORDER BY purchaseID ASC;

-- populate dropdown for selection of Medications on Purchases page
SELECT medicationID, brandName FROM Medications;

-- Insert a new purchase
INSERT INTO Purchases (medicationID, customerID, dateOfPurchase)
VALUES (:medicationID, :customerID, :dateOfPurchase);

-- populate dropdown for selection of Customers on Purchases page
SELECT customerID, CONCAT(customerID, ' - ', lastName, ', ', firstName) AS customerDisplay
FROM Customers;

-- populate dropdown for selection of Medications on Purchases page
SELECT medicationID, brandName, strength, formulation
FROM Medications;

-- Delete a purchase
DELETE FROM Purchases WHERE purchaseID = :purchaseID;

-- get purchase to update
SELECT * FROM Purchases WHERE purchaseID = :purchaseID;

-- Get medication information for update
SELECT medicationID, brandName, genericName from Medications;

-- Get customer information for update
SELECT customerID, firstName, lastName from Customers;

-- Update purchase
UPDATE Purchases
    SET medicationID = :medicationIDInput,
        customerID = :customerIDInput,
        lastPurchased = :lastPurcasedInput
    WHERE purchaseID = :purcahseIDInput;


-- Customers Page
-- get all Customers
SELECT customerID, firstName, lastName, email, phoneNumber
FROM Customers;

-- add Customer
INSERT INTO Customers (firstName, lastName, email, phoneNumber) 
VALUES (:firstNameInput, :lastNameInput, :emailInput, :phoneNumberInput);

-- Get Customer that is to be updated
SELECT * FROM Customers WHERE customerID = :customerID

-- Insert Customer into database
INSERT INTO Customers (firstName, lastName, email, phoneNumber)
VALUES (:firstName, :lastName, :email, :phoneNumber)

-- update Customer data
UPDATE Customers 
SET firstName = :firstNameInput, 
    lastName = :lastNameInput, 
    email = :emailInput, 
    phoneNumber = :phoneNumberInput
WHERE customerID = :customerIDInput;

-- NULLable attributes
UPDATE Customers
SET email = NULL
WHERE customerID = :customerIDInput;

UPDATE Customers
SET phoneNumber = NULL
WHERE customerID = :customerIDInput;
