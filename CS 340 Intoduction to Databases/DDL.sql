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

-- This file is to setup the database


-- Disable commits and foreign key checks
SET FOREIGN_KEY_CHECKS = 0;
SET AUTOCOMMIT = 0;


-- Drop tables if they exist
DROP TABLE IF EXISTS Medications;
DROP TABLE IF EXISTS Automations;
DROP TABLE IF EXISTS Refrigerators;
DROP TABLE IF EXISTS Inventories;
DROP TABLE IF EXISTS Purchases;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Prescriptions;
DROP TABLE IF EXISTS Wholesalers;

-- Create Medications, Inventories, Purchases, Customers and Prescriptions tables.
CREATE TABLE Wholesalers (
    wholesalerID int NOT NULL AUTO_INCREMENT,
    wholesalerName varchar(255) NOT NULL,
    contactName varchar(255),
    contactEmail varchar(255),
    contactPhoneNumber varchar(255),
    address varchar(255),
    PRIMARY KEY (wholesalerID)
);

CREATE TABLE Medications (
    medicationID int NOT NULL AUTO_INCREMENT,
    brandName varchar(255) NOT NULL,
    genericName varchar(255),
    strength varchar(255) NOT NULL,
    formulation varchar(255) NOT NULL,
    upcNumber varchar(12) NOT NULL,
    ndcNumber varchar(11) NOT NULL UNIQUE,
    costToBuy float,
    bottleCountSize varchar(255) NOT NULL,
    wholesalerID int,
    lastPurchased date,
    CHECK (length(ndcNumber) = 11 AND ndcNumber REGEXP '^[0-9]+$'),
    PRIMARY KEY (medicationID),
    FOREIGN KEY (wholesalerID) REFERENCES Wholesalers(wholesalerID)
);

-- Create Automation table
CREATE TABLE Automations (
    automationID int NOT NULL AUTO_INCREMENT,
    automationName varchar(255) NOT NULL,
    PRIMARY KEY (automationID)
);

-- Create Refrigerator Table
CREATE TABLE Refrigerators (
    refrigeratorID int NOT NULL AUTO_INCREMENT,
    refrigeratorName varchar(255) NOT NULL,
    PRIMARY KEY (refrigeratorID)
);

-- Create Inventories table
CREATE TABLE Inventories (
    inventoryID int NOT NULL AUTO_INCREMENT,
    medicationID int,
    currentInventory int,
    minInventory int,
    maxInventory int,
    locationShelf varchar(255),
    locationBox varchar(255),
    locationAutomation int,
    locationInRefrigerator int,
    PRIMARY KEY (inventoryID),
    FOREIGN KEY (medicationID) REFERENCES Medications(medicationID) ON DELETE CASCADE,
	FOREIGN KEY (locationAutomation) REFERENCES Automations(automationID),
	FOREIGN KEY (locationInRefrigerator) REFERENCES Refrigerators(refrigeratorID)
);

-- Create Customers table
CREATE TABLE Customers (
    customerID int NOT NULL AUTO_INCREMENT,
    firstName varchar(255) NOT NULL,
    lastName varchar(255) NOT NULL,
    email varchar(255) UNIQUE,
    phoneNumber varchar(255),
    PRIMARY KEY (customerID)
);

-- Create Purchases table
CREATE TABLE Purchases (
    purchaseID int NOT NULL AUTO_INCREMENT,
    medicationID int,
    customerID int,
    dateOfPurchase date NOT NULL,
    PRIMARY KEY (purchaseID),
    FOREIGN KEY (medicationID) REFERENCES Medications(medicationID) ON DELETE CASCADE,
    FOREIGN KEY (customerID) REFERENCES Customers(customerID) ON DELETE CASCADE
);

-- Insert data into tables.
INSERT INTO Wholesalers (wholesalerName, contactName, contactEmail, contactPhoneNumber, address) VALUES
('Dharma Pharma', 'Desmond Hume', 'dhume@dharma.com', '555-0123', '108 Main St'),
('InGen Medical Innovations', 'John Hammond', 'jhammond@ingen.com', '555-0223', 'Jurassic Park'),
('Krusty Krab Health Solutions', 'Eugene Krabs', 'mkrabs@krustykrab.com', '555-0323', 'Bikini Bottom'),
('Stark Health Tech', 'Tony Stark', 'tstark@starkindustries.com', '555-0423', '10880 Malibu Point');

INSERT INTO Automations (automationName)
VALUES 
('Robot1'),
('Robot2'),
('Robot3');

INSERT INTO Refrigerators (refrigeratorName)
VALUES 
('fridge1'),
('fridge2'),
('fridge3');

INSERT INTO Customers (firstName, lastName, email, phoneNumber) VALUES
('Walter', 'White', 'heisenberg@gmail.com', '123-456-7890'),
('Jesse', 'Pinkman', 'jesse@hotmail.com', '623-765-4321'),
('Saul', 'Goodman', 'bettercallsaul@outlook.com', '321-654-9870'),
('Benjamin', 'Linus', 'thothers@yahoo.com', '602-765-4321');

INSERT INTO Medications (brandName, genericName, strength, formulation, upcNumber, ndcNumber, costToBuy, bottleCountSize, wholesalerID, lastPurchased)
VALUES 
('Advil', 'Ibuprofen', '200mg', 'Tablet', '123456789123', '12345678913', 10.00, '100', 
    (SELECT wholesalerID FROM Wholesalers WHERE wholesalerName = 'Dharma Pharma'), '2023-10-01'),
('Tylenol', 'Acetaminophen', '500mg', 'Tablet', '965135494562', '96513549456', 15.23, '100', 
    (SELECT wholesalerID FROM Wholesalers WHERE wholesalerName = 'InGen Medical Innovations'), '2023-09-15'),
('ProAir', 'Albuterol', '90mcg', 'Inhaler', '136549513546', '12364864521', 23.5, '1000', 
    (SELECT wholesalerID FROM Wholesalers WHERE wholesalerName = 'Krusty Krab Health Solutions'), '2023-10-10'),
('Aleve', 'Naproxen', '220mg', 'Tablet', '845612365475', '45632146594', 8.99, '100', 
    (SELECT wholesalerID FROM Wholesalers WHERE wholesalerName = 'Stark Health Tech'), '2023-09-10');

INSERT INTO Inventories (
  medicationID, 
  currentInventory, 
  minInventory, 
  maxInventory, 
  locationShelf, 
  locationBox, 
  locationAutomation, 
  locationInRefrigerator
)
VALUES 
(
  (SELECT medicationID FROM Medications WHERE brandName ='Advil'), 
  50, 
  10, 
  100, 
  'A1', 
  'B2', 
  (SELECT automationID FROM Automations WHERE automationName = 'Robot1'), 
  NULL
),
(
  (SELECT medicationID FROM Medications WHERE brandName ='Tylenol'), 
  30, 
  5, 
  50, 
  'A2', 
  'B3', 
  (SELECT automationID FROM Automations WHERE automationName = 'Robot1'), 
  NULL
),
(
  (SELECT medicationID FROM Medications WHERE brandName ='ProAir'), 
  20, 
  2, 
  25, 
  'A3', 
  'B4', 
  NULL, 
  (SELECT refrigeratorID FROM Refrigerators WHERE refrigeratorName = 'fridge1')
),
(
  (SELECT medicationID FROM Medications WHERE brandName ='Aleve'), 
  60, 
  10, 
  120, 
  'A4', 
  'B5', 
  (SELECT automationID FROM Automations WHERE automationName = 'Robot1'), 
  NULL
);

INSERT INTO Purchases (medicationID, customerID, dateOfPurchase)
VALUES 
((SELECT medicationID FROM Medications WHERE brandName ='Advil'), 
    (SELECT customerID FROM Customers WHERE lastName ='White' AND firstName = 'Walter'),
    '2023-10-05'),
((SELECT medicationID FROM Medications WHERE brandName ='Tylenol'), 
    (SELECT customerID FROM Customers WHERE lastName ='Pinkman' AND firstName = 'Jesse'), 
    '2023-10-06'),
((SELECT medicationID FROM Medications WHERE brandName ='ProAir'), 
    (SELECT customerID FROM Customers WHERE lastName ='Goodman' AND firstName = 'Saul'), 
    '2023-10-07'),
((SELECT medicationID FROM Medications WHERE brandName ='Aleve'), 
    (SELECT customerID FROM Customers WHERE lastName ='Linus' AND firstName = 'Benjamin'), 
    '2023-10-06');


-- Enable commits and foreign key checks.
SET FOREIGN_KEY_CHECKS=1;
COMMIT;