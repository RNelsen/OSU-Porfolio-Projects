'use strict'

function addStaffToTable(staff) {
    generatedStaff.innerHTML += `
    <tr class="randomStaff">
        <td><img src=${staff.picture.thumbnail} alt="Random Staff"/></td>
        <td><a href="mailto:${staff.email}">
            ${staff.name.first}
            ${staff.name.last}</a>
        </td>
        <td>${staff.phone}</td>
        <td>${staff.location.city}</td>
    </tr>
    `;
};

async function retrieveStaff(trigger) {
    trigger.preventDefault();
    const staffId = trigger.target.getAttribute('id');

    const url = staffId === 'browserGenerated' ? "https://randomuser.me/api/" : "/random-staff"

    try {
        const returned = await fetch(url);
        const information = await returned.json();
        
        if (returned.status == 200) {
            addStaffToTable(information.results[0]);
        }
    } catch(error) {
        console.error(error)
    }
};

document.addEventListener('DOMContentLoaded', () => {
    const browser = document.getElementById('browserGenerated');
    browser.addEventListener('click', retrieveStaff);

    const server = document.getElementById('serverGenerated');
    server.addEventListener('click', retrieveStaff)
});