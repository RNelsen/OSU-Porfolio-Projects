// Import dependencies.
import mongoose from 'mongoose';
import 'dotenv/config';

// Connect based on the .env file parameters.
mongoose.connect(
    process.env.MONGODB_CONNECT_STRING,
    { useNewUrlParser: true }
);
const db = mongoose.connection;

// Confirm that the database has connected and print a message in the console.
db.once("open", (err) => {
    if(err){
        res.status(500).json({ error: '500:Connection to the server failed.' });
    } else  {
        console.log('Successfully connected to MongoDB Movies collection using Mongoose.');
    }
});

// SCHEMA: Define the collection's schema.
const medSchema = mongoose.Schema({
	medName:    { type: String, required: true },
    numTablets: { type: Number, required: true },
	date:       { type: Date, required: true, min: '2023-03-06', default: Date.now }
});

// Compile the model from the schema.
const Med = mongoose.model('Med', medSchema);


// CREATE model *****************************************
const createMed = async (medName, numTablets, date) => {
    const med = new Med({ 
        medName: medName, 
        numTablets: numTablets, 
        date: date 
    });
    return med.save();
}


// RETRIEVE models *****************************************
// Retrieve based on a filter and return a promise.
const retrieveMed = async () => {
    const query = Med.find();
    return query.exec();
}

// RETRIEVE by ID
const retrieveMedByID = async (_id) => {
    const query = Med.findById({_id: _id});
    return query.exec();
}

// DELETE model based on _id  *****************************************
const deleteMedById = async (_id) => {
    const result = await Med.deleteOne({_id: _id});
    return result.deletedCount;
};


// UPDATE model *****************************************************
const updateMed = async (_id, medName, numTablets, date) => {
    const result = await Med.replaceOne({_id: _id }, {
        medName: medName,
        numTablets: numTablets,
        date: date
    });
    return { 
        _id: _id, 
        medName: medName,
        numTablets: numTablets,
        date: date 
    }
}



// Export our variables for use in the controller file.
export { createMed, retrieveMed, retrieveMedByID, updateMed, deleteMedById }