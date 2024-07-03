import React, { useState }  from 'react';
import { useNavigate } from "react-router-dom";

export const EditMedPage = ({ medToEdit }) => {
 
    const [medName, setMedName] = useState(medToEdit.medName);
    const [numTablets, setNumTablets] = useState(medToEdit.numTablets);
    const [date, setDate] = useState(medToEdit.date.slice(0,10));
    
    const redirect = useNavigate();

    const editMed = async () => {
        const response = await fetch(`/meds/${medToEdit._id}`, {
            method: 'PUT',
            body: JSON.stringify({ 
                medName: medName, 
                numTablets: numTablets, 
                date: date
            }),
            headers: {'Content-Type': 'application/json',},
        });

        if (response.status === 200) {
            alert(`Medication Updated`);
        } else {
            const errMessage = await response.json();
            alert(`Error happened so medication was not updated.  Error code ${response.status}. ${errMessage.Error}`);
        }
        redirect("/meds");
    }

    return (
        <>
        <article>
            <h2>Edit a medication</h2>
            <p className="paragraphOffset"> Please edit the medication listed below and then hit submit.</p>
            <form onSubmit={(e) => { e.preventDefault();}}>
                <fieldset>
                    <legend>Medication to Edit</legend>
                    <label for="medName">Medication Name</label>
                    <input
                        type="text"
                        value={medName}
                        onChange={e => setMedName(e.target.value)} 
                        id="exmedName" />
                    
                    <label for="numTablets">Number of Tablets</label>
                    <input
                        type="number"
                        value={numTablets}
                        onChange={e => setNumTablets(e.target.value)} 
                        id="exnumTablets" />

                    <label for="date">Date Last Refilled</label>
                    <input
                        type="date"
                        placeholder="date"
                        value={date}
                        onChange={e => setDate(e.target.value)} 
                        id="exdate" />

                    <label for="submit">
                    <button
                        onClick={editMed}
                        id="exsubmit"
                    >Save</button> updates to the collection</label>
                </fieldset>
                </form>
            </article>
        </>
    );
}
export default EditMedPage;