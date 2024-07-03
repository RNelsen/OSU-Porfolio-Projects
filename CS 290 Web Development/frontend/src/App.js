
import React from 'react';
import { useState} from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import products from './data/products.js';


import Nav from './components/Nav.js';
// import ContactPage from './pages/ContactPage';
import TopicPage from './pages/TopicPage.js';
import GalleryPage from './pages/GalleryPage.js';
import StaffPage from './pages/StaffPage.js';
import OrderPage from './pages/OrderPage.js';
import HomePage from './pages/HomePage.js';
import MedPage from './pages/MedPage.js';
import AddMedPage from './pages/AddMedPage.js';
import EditMedPage from './pages/EditMedPage.js';


import './App.css';

function App() {

    const [medEdit, setMedtoeEdit] = useState([]);

  return (  
    <div className="App">
      <BrowserRouter>

        <header className="App-header">
          <h1>Daniel Reid Nelsen's CS 290 Webpage 
            {/* <img src={logo} className="App-logo" alt="logo" /> */}
          </h1>
        </header>

        <Nav />

        <main>
          <section>
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/topics" element={<TopicPage />} />
                <Route path="/meds" element={<MedPage setMed = {setMedtoeEdit} />} />
                <Route path="/gallery" element={<GalleryPage />} /> 
                <Route path="/staff" element={<StaffPage />} /> 
                <Route path="/add" element={<AddMedPage />} /> 
                <Route path="/edit" element={<EditMedPage medToEdit={medEdit}/>} /> 
                <Route path="/order" element={<OrderPage products={products}/>} /> 
            </Routes>
          </section>
        </main>
        
        <footer>
          <p>&copy; 2023 Daniel Reid Nelsen</p>
        </footer>
        
        </BrowserRouter>
      </div>
    );
  }

export default App;