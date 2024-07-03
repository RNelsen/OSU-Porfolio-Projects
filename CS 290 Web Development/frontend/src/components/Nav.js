//Navigate from page to page

import React from 'react';
import { Link } from 'react-router-dom';


function Nav() {
  return (
    <nav className="App-nav">
        <Link to="/">Home</Link>
        <Link to="../topics">Web Topics</Link>
        <Link to="../meds">Med List</Link>
        <Link to="../gallery">Gallery</Link>
        {/* <Link to="../contact">Contact</Link> */}
        <Link to="../order">Order</Link>
        <Link to="../staff">Staff</Link>
    </nav>
  );
}

export default Nav;
