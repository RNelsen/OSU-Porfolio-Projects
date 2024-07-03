import React from 'react';
import ProductQuantity from './ProductQuantity.js';


function ProductRow( {product}) {
    return (
        <>
            <tr>
                <td><strong>{product.product}</strong> by {product.company}</td>
                <td>{product.price.toLocaleString("en-US", {style: "currency", currency: 'USD'})}</td>
                <td className="tableCenter"><ProductQuantity /></td>
            </tr>
        </>
    )
}

export default ProductRow;