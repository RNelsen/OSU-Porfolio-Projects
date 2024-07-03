import { React, useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

import MedList from '../components/MedList.js';
// import EditMedPage from './EditMedPage.js';

function MedPage({ setMed }) {
    // Use the Navigate for redirection
    const redirect = useNavigate();

    // Use state to bring in the data
    const [meds, setMeds] = useState([]);

    // RETRIEVE the entire list of medications
    const loadMeds = async () => {
        const response = await fetch('/meds');
        const meds = await response.json();
        setMeds(meds);
    } 

    // UPDATE a single medication
    const onEditMed = async med => {
        setMed(med);
        redirect("/edit");
    }

    // // Add a single medication
    // const onAddMed = async med => {
    //     setMeds(med);
    //     redirect("/add");
    // }


    // DELETE a single medication  
    const onDeleteMed = async _id => {
        const response = await fetch(`/meds/${_id}`, { method: 'DELETE' });
        if (response.status === 204) {
            const getResponse = await fetch('/meds');
            const meds = await getResponse.json();
            setMeds(meds);
        } else {
            console.error(`So an error happened and medication was not deleted.  Error code code = ${response.status}`)
        }
    }

    // LOAD all the medications
    useEffect(() => {
        loadMeds();
    }, []);

    // DISPLAY the medications
    return (
        <>
            <h2>List of Medications</h2>
            <p className="paragraphOffset">Page to log when mediciations they were last filled by the pharmacy. 
            Add medications by clicking the icon next to add.  Medications can be deleted or edited as well.</p> 
            <MedList 
                meds={meds} 
                onEdit={onEditMed}
                onDelete={onDeleteMed}
            />
        </>
    );
}

export default MedPage;