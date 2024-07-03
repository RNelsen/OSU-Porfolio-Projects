// 'use strict';

// const express = require('express');
// const app = express();
// const PORT = process.env.PORT;
// const products = require('./products.js').products;

import express from 'express';
import fetch from 'node-fetch';
import 'dotenv/config';
import asyncHandler from 'express-async-handler';
import {products} from './products.js';

const PORT = process.env.PORT
const app = express();

app.use(express.urlencoded( {
    extended: true
}));

app.use(express.static('public'));

let htmlTop = `
<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Daniel Reid Nelsen</title>
    <meta name="robots" content="noindex, noarchive, nofollow">
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <link rel='stylesheet' type='text/css' media='screen' href='main.css'>
    <script src='main.js'></script>
</head>
<body>
    <header>
        <h1>Daniel Reid Nelsen</h1>
    </header>
    <nav>
        <a href="index.html">Home</a>
        <a href="gallery.html">Gallery</a>
        <a href="contact.html">Contact</a>
        <a href="order.html">Order</a>
        <a href="staff.html">Staff</a>
    </nav>
    <main>
`;

let htmlBottom = `

    </main>
    <footer>
        <p>&copy 2023 Daniel Reid Nelsen</p>
    </footer>
</body>
</html>
`; 

function joinAnimals(chosen) {
    switch(typeof chosen) {
        case "object":  
          return chosen.join(`, `); 
        case "string":  
           return chosen; 
        default:  
           return " No aminals chosen."; 
    }
  }

app.post("/results", (req, res) => {
    const name = req.body.firstLastName;

    const nameCap = name.split(" ");

    for (let i = 0; i < nameCap.length; i++) 
    {
        nameCap[i] = nameCap[i][0].toUpperCase() + nameCap[i].substr(1);
    };

    const nameCapFinal = nameCap.join(" ");

    const email = req.body.emailAddress;
    const radio = req.body.radioBox;
    const degree = req.body.degree;
    const animals = req.body.check;
    const animalsJoin = joinAnimals(animals);
    const message = req.body.feedback;

    res.send( `${htmlTop}
    <section>
        <h2>Contact</h2>
            <article>
                <p class="paragraphOffset">Hello ${nameCapFinal}, Thank You for the Feedback!</p>
                <p class="paragraphOffset">I see that you picked the following items about yourself.  Your first
                degree was in <strong>${degree}</strong>. You found this website by
                utilizing the following method: <strong>${radio}</strong>. Finally, you 
                like the following animals: <strong>${animalsJoin}</strong>.</p>
            </article>
        </section>

        ${htmlBottom}`);

    const emailer = (`<p>Hi <strong>${nameCapFinal}</strong>,</p> <p>Thank you for the feedback.
    Here is the message that you left on the webpage: <p><strong>${message}</strong></p>  
    I hope this message finds you well at your email address of <strong>${email}</strong>.</p>

    <p>Have a nice day!  Danield Reid Nelsen</p>`);

    const nodemailer = require("nodemailer");

    async function main() {
            // Generate test SMTP service account from ethereal.email
            // Only needed if you don't have a real mail account for testing
            let testAccount = await nodemailer.createTestAccount();
          
            // create reusable transporter object using the default SMTP transport
            let transporter = nodemailer.createTransport({
              host: "smtp.ethereal.email",
              port: 587,
              secure: false, // true for 465, false for other ports
              auth: {
                user: testAccount.user, // generated ethereal user
                pass: testAccount.pass, // generated ethereal password
              },
            });
          
            // send mail with defined transport object
            let info = await transporter.sendMail({
              from: '"Daniel Reid Nelsen" <nelsenda@oregonstate.edu>', // sender address
              to: email, // list of receivers
              subject: "Hello ✔", // Subject line
            //   text: "Hello nameCapFinal" , // plain text body
              html: emailer, // html body
            });
          
            console.log("Message sent: %s", info.messageId);
            // Message sent: <b658f8ca-6296-ccf4-8306-87d57a0b4321@example.com>
          
            // Preview only available when sending through an Ethereal account
            console.log("Preview URL: %s", nodemailer.getTestMessageUrl(info));
            // Preview URL: https://ethereal.email/message/WaQKMgKddxQDoou...
          }
        
    main().catch(console.error);
});


function userInput(chosenProduct) {
    for (const item of products) {
        if (item.product === chosenProduct) {
            // console.log(typeof(item.product));
            return item.price
        }
    };
    return 0;
};

app.post("/finalorder", (req, res) => {
    const name = req.body.firstLastName;
    const email = req.body.emailAddress;
    const address = req.body.physicalAddress;
    const instructions = req.body.delivery;
    const pickedProduct = req.body.radioBox;
    const itemQuantity = parseInt(req.body.quantity);

    const price = userInput(pickedProduct);
    const cost = price * itemQuantity;
    const numFormatted = cost.toLocaleString("en-US", {style:"currency", currency:"USD"});

    const formattedQuantity = itemQuantity.toLocaleString()

    const nameCap = name.split(" ");

    for (let i = 0; i < nameCap.length; i++) 
    {
        nameCap[i] = nameCap[i][0].toUpperCase() + nameCap[i].substr(1);
    };

    const nameCapFinal = nameCap.join(" ");

    res.send( `${htmlTop}
        <section>
            <h2>Order</h2>
            <article>
                <p class="paragraphOffset">Hello <strong>${nameCapFinal}</strong>, Thank You order!</p>
                <p class="paragraphOffset">Your order for <strong>${formattedQuantity}</strong> item(s) of 
                <strong>${pickedProduct}</strong> will cost <strong>${numFormatted}</strong>.</p>
                <p class="paragraphOffset">This order will be delivered to <strong>${address}</strong>
                with the following delivery instructions: <strong>${instructions}</strong></p>
                <p class="paragraphOffset">If there is a delay with your order, we will 
                reach out to you at <strong>${email}</strong>.</p>
                <p class="paragraphOffset">Have a great day!</p>
            </article>
        </section>
        ${htmlBottom}`);

});


// counter for extra credit Assignment 6
const printToConsole = 10;
let apiCounter = 0;

app.use('/random-staff', (req, res, next) => {

    apiCounter += 1;

    if (apiCounter % printToConsole === 0) {
        console.log(`Total number of retrieved requests from RandomUser website is ${apiCounter}.`);
    }
    next();
});



app.get('/random-staff', asyncHandler(async (req, res) => {
    const returned = await fetch('https://randomuser.me/api/');
    const information = await returned.json();

    res.send(information);
}));

app.use((err, req, res, next) => {
    console.error(err.stack)
    res.status(500).send(`<h2>YUP</h2><p>So, we encountered an error Houston.  Please try again.</p>`);
});

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}...`);
});