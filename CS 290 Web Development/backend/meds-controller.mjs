import 'dotenv/config';
import express from 'express';
import * as meds from './meds-model.mjs';

const PORT = process.env.PORT;
const app = express();
app.use(express.json());  // REST needs JSON MIME type.


// CREATE controller ******************************************
app.post ('/meds', (req,res) => { 
    meds.createMed(
        req.body.medName, 
        req.body.numTablets, 
        req.body.date
        )
        .then(meds => {
            res.status(201).json(meds);
        })
        .catch(error => {
            console.log(error);
            res.status(400).json({ error: 'create a document failed' });
        });
});


// RETRIEVE controller ****************************************************
app.get('/meds', (req, res) => {
    meds.retrieveMed()
        .then(meds => { 
            if (meds !== null) {
                res.json(meds);
            } else {
                res.status(404).json({ Error: 'document not found.' });
            }         
         })
        .catch(error => {
            console.log(error);
            res.status(400).json({ Error: 'retrieve document failed.' });
        });
});


// RETRIEVE by ID controller
app.get('/meds/:_id', (req, res) => {
    meds.retrieveMedByID(req.params._id)
    .then(meds => { 
        if (meds !== null) {
            res.json(meds);
        } else {
            res.status(404).json({ Error: 'document not found' });
        }         
     })
    .catch(error => {
        console.log(error);
        res.status(400).json({ Error: 'retrieve document failed' });
    });

});


// UPDATE controller ************************************
app.put('/meds/:_id', (req, res) => {
    meds.updateMed(
        req.params._id, 
        req.body.medName, 
        req.body.numTablets, 
        req.body.date
    )
    .then(meds => {
        res.json(meds);
    })
    .catch(error => {
        console.log(error);
        res.status(400).json({ error: 'document update failed' });
    });
});


// DELETE Controller ******************************
app.delete('/meds/:_id', (req, res) => {
    meds.deleteMedById(req.params._id)
        .then(deletedCount => {
            if (deletedCount === 1) {
                res.status(204).send();
            } else {
                res.status(404).json({ Error: 'document no longer exists' });
            }
        })
        .catch(error => {
            console.error(error);
            res.send({ error: 'delete a document failed' });
        });
});


app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}...`);
});