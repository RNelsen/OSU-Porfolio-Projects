import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";

export const AddMedPage = () => {

    const [medName, setMedName] = useState('');
    const [numTablets, setNumTablets] = useState('');
    const [date, setDate] = useState('');
    
    const redirect = useNavigate();

    const addMed = async () => {
        const newMed = { medName, numTablets, date };
        const response = await fetch('/meds', {
            method: 'post',
            body: JSON.stringify(newMed),
            headers: {
                'Content-Type': 'application/json',
            },
        });
        if(response.status === 201){
            alert(`Medication added`);
            redirect("/meds");
        } else {
            alert(`So an error happend and the medication was not added.  Error code = ${response.status}`);
            redirect("/meds");
        }
    };


    return (
        <>
        <article>
            <h2>Add a medication to your regime</h2>
            <p className="paragraphOffset">Add medication parameters below and the hit submit.</p>
            <form onSubmit={(e) => { e.preventDefault();}}>
                <fieldset>
                    <legend>Medication to be added</legend>
                    <label for="title">Drug Name</label>
                    <input
                        type="text"
                        placeholder="Name of Medication"
                        value={medName}
                        required
                        onChange={e => setMedName(e.target.value)} 
                        id="medName" />
                    
                    <label for="year">Number of tablets refilled</label>
                    <input
                        type="number"
                        value={numTablets}
                        placeholder="number of tablets"
                        required
                        onChange={e => setNumTablets(e.target.value)} 
                        id="numTablets" />

                    <label for="language">Date Refilled</label>
                    <input
                        type="date"
                        placeholder="date"
                        value={date}
                        onChange={e => setDate(e.target.value)} 
                        id="date" />

                    <label for="submit">
                    <button
                        type="submit"
                        onClick={addMed}
                        id="submit"
                    >Add</button> to the collection</label>
                </fieldset>
                </form>
            </article>
        </>
    );
}

export default AddMedPage;