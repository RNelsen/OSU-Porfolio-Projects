import React from 'react';

import { RiDeleteBin5Line, RiFileEditLine } from 'react-icons/ri';


function Med({ med, onEdit, onDelete }) {
    
    return (
        <tr> 
            <td>{med.medName}</td>
            <td className="tableCenter">{med.numTablets}</td>
            <td className="tableCenter">{med.date.slice(0,10)}</td>
            <td className="tableCenter"><RiDeleteBin5Line onClick={() => onDelete(med._id)} /></td>
            <td className="tableCenter"><RiFileEditLine onClick={() => onEdit(med)} /></td>
        </tr>
    );
}

export default Med;