import React from "react";

import ImageGallery from 'react-image-gallery';

const images = [
    {
        original: 'images/arches-national-park-1.jpg',
        thumbnail: 'images/arches-national-park-1.jpg',
        description: 'Double Arch in Arches National Park Utah, USA. Taken in 2019.',
        originalHeight: '500px'
    },
    {
        original: 'images/arches-national-park-2.jpg',
        thumbnail: 'images/arches-national-park-2.jpg',
        description: 'Double Arch in Arches National Park Utah, USA. Taken in 2019.',
        originalHeight: '500px'
    },
    {
        original: 'images/bryce-canyon-1.jpg',
        thumbnail: 'images/bryce-canyon-1.jpg',
        description: 'Bryce Canyon, Utah, USA. Taken in 2019.',
        originalHeight: '500px',
    },
    {
        original: 'images/shoshone-falls-idaho.jpg',
        thumbnail: 'images/shoshone-falls-idaho.jpg',
        description: 'Shoshone Falls in Twin Falls Idaho, USA. Taken in 2019.',
        originalHeight: '500px',
    },
    {
        original: 'images/chihuly-glass-art-7.jpg',
        thumbnail: 'images/chihuly-glass-art-7.jpg',
        description: 'Chihuly glass sculpture in the Chihuly Garden and Glass Exhibit Seattle, WA, USA. Taken in 2018.',
        originalHeight: '500px',
    },
    {
        original: 'images/chihuly-glass-art-1.jpg',
        thumbnail: 'images/chihuly-glass-art-1.jpg',
        description: 'Chihuly glass sculpture in the Chihuly Garden and Glass Exhibit Seattle, WA, USA. Taken in 2018.',
        originalHeight: '500px',
    },
    {
        original: 'images/chihuly-glass-art-2.jpg',
        thumbnail: 'images/chihuly-glass-art-2.jpg',
        description: 'Chihuly glass sculpture in the Chihuly Garden and Glass Exhibit Seattle, WA, USA. Taken in 2018.',
        originalHeight: '500px',
    },
    {
        original: 'images/chihuly-glass-art-3.jpg',
        thumbnail: 'images/chihuly-glass-art-3.jpg',
        description: 'Chihuly glass sculpture in the Chihuly Garden and Glass Exhibit Seattle, WA, USA. Taken in 2018.',
        originalHeight: '500px',
    },
    {
        original: 'images/chihuly-glass-art-4.jpg',
        thumbnail: 'images/chihuly-glass-art-4.jpg',
        description: 'Chihuly glass sculpture in the Chihuly Garden and Glass Exhibit Seattle, WA, USA. Taken in 2018.',
        originalHeight: '500px',
    },
    {
        original: 'images/chihuly-glass-art-5.jpg',
        thumbnail: 'images/chihuly-glass-art-5.jpg',
        description: 'Chihuly glass sculpture in the Chihuly Garden and Glass Exhibit Seattle, WA, USA. Taken in 2018.',
        originalHeight: '500px',
    },
]

function GalleryPage() {
    return (
        <>
            <h2>Visited Plages</h2>
            <p className="articleClass">Places that I visited in the past.</p>
            <article>
                <ImageGallery items={images}/>

            </article>
        </>

    );
}

export default GalleryPage;