import React, { useState } from "react";
// import { TfiAngleDown, TfiAngleUp } from 'react-icons/tfi';
// import { AiOutlineArrowDown, AiOutlineArrowUp } from 'react-icons/ai';
import { FcDown, FcUp } from 'react-icons/fc';


function ProductQuantity() {
    const [quantity, getQuantity] = useState(0);
    const increment = () => getQuantity(quantity === 10 ? quantity : quantity + 1);
    const decrement = () => getQuantity(quantity === 0 ? 0 : quantity - 1);

    return (
        <>
            <FcUp onClick={increment} />
            <span>{quantity}</span>
            <FcDown onClick={decrement} />
        </>
    );
}

export default ProductQuantity;