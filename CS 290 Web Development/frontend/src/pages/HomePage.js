import React from "react";

function HomePage() {
    return (
        <>
        <h2>WEB DEVELOPMENT TOPICS</h2>
        <h3 class="paragraphOffset">Technologies Used on This Website</h3>
        <p class="paragraphOffset">This website utilizes several technologies.  The list below outlines 
            the technologies used.  
        </p>
        <dl id="fiveE" class="articleClass">
            <dt><strong>HTML</strong></dt>
            <dd>Usage of basic HTML markup to form the backbone of the webpages</dd>
            <dt><strong>CSS</strong></dt>
            <dd>Cascading Style Sheets to create uniqueness and style on the pages</dd>
            <dt><strong>Icons</strong></dt>
            <dd>Use of REACT icons to bring in style to the page</dd>
            <dt><strong>Express</strong></dt>
            <dd>Express to serve a dynamic content</dd>
            <dt><strong>Google Fonts</strong></dt>
            <dd>Use of fonts from Google</dd>
            <dt><strong>JavaScript</strong></dt>
            <dd>Programming language to used to create interactive webpages</dd>
            <dt><strong>MongoDB</strong></dt>
            <dd>Backend database to store data</dd>
            <dt><strong>Node.js</strong></dt>
            <dd>Open-source, cross-platform JavaScript runtime</dd>
            <dt><strong>Mongoose</strong></dt>
            <dd>Node plugin to connect to MongoDB</dd>
            <dt><strong>Optimized Images</strong></dt>
            <dd>Images are optimized for quick downloading</dd>
            <dt><strong>REACT</strong></dt>
            <dd>A free and open-source front-end JavaScript library to create user interfaces.  Created by Meta</dd>
            <dt><strong>Rest API</strong></dt>
            <dd>This is an application programming interface that used for RESTful web services</dd>
        </dl>
        </>
    );
}

export default HomePage;