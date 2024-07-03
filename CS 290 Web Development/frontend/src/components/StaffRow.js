import React from "react";

function StaffRow({ person }) {
    return ( 
        <tr className="randomStaff">
        <td><img src={person.picture.thumbnail} alt="Random Staff"/></td>
        <td><a href={"mailto:" + person.email}>
            {person.name.first} {person.name.last}</a>
        </td>
        <td>{person.phone}</td>
        <td>{person.location.city}</td>
    </tr>
    );
}

export default StaffRow;
