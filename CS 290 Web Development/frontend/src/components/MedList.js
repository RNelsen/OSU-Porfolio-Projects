import React from 'react';
import Med from './Med.js';
import { useNavigate } from 'react-router-dom';

import { BiMessageSquareAdd } from 'react-icons/bi';
import { RiFileEditLine } from 'react-icons/ri';

function MedList({ meds, onDelete, onEdit }) {

    const redirect = useNavigate();

    const navToAdd = () => {
        redirect("/add");
    };

    return (
        <table id="meds">
            <caption>Add <BiMessageSquareAdd onClick={navToAdd} /> and Edit Medications </caption >
            <thead>
                <tr>
                    <th>Medication</th>
                    <th>Number of Tablets</th>
                    <th>Date</th>
                    <th>Delete</th>
                    <th>Edit</th>
                </tr>
            </thead>
            <tbody>
                {meds.map((med, i) => 
                    <Med 
                        med={med}
                        key={i}
                        onDelete={onDelete}
                        onEdit={onEdit}
                    />)}
            </tbody>
        </table>
    );
}

export default MedList;
