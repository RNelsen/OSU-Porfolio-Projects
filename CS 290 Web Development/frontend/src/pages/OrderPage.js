import React from "react";
import ProductRow from '../components/ProductRow.js';

function OrderPage ({ products }) {  
    return (
        <>
        <h2>Order Page</h2>
        <article>
                <p className="paragraphOffset">
                    From this page, please select items to be ordered.  Up to 10 
                    per item. 
                </p>
                <table id="productTable">
                    <caption>Items to be purchased</caption>
                    <thead>
                        <tr>
                            <th>Item, company</th>
                            <th>Price</th>
                            <th>Quantity</th>
                        </tr>
                    </thead>
                    <tbody>
                        {products.map((itemForPurhcase, index) =>
                            <ProductRow
                            product={itemForPurhcase}
                            key={index}
                            />
                        )}
                    </tbody>
                    <tfoot></tfoot>

                </table>
        </article>
        </>
    );
};

export default OrderPage;