import React, { useContext, useState } from 'react';
import { AppContext } from '../context/AppContext';
import '../App.css';

const Currency = () => {
    const { currency, dispatch } = useContext(AppContext);
    const [ , setNewCurrency] = useState(currency);

    const handleCurrencyChange = (event) => {
        const updatedCurrency = (event.target.value);
        setNewCurrency(updatedCurrency);
        dispatch({
            type: 'CHG_CURRENCY',
            payload: updatedCurrency,
        });
    };

    return (
        <div className='alert alert-secondary'>
        <div className="select-wrapper" data-currency={currency}>
            <htmltag className="select-label">Currency: </htmltag>
            <select className= "currency-select" id="currency" value={currency} class="selector" onChange={handleCurrencyChange}>
                <option value="$"> $ Dollar</option>
                <option value="£"> £ Pound</option>
                <option value="€"> € Euro</option>
                <option value="₹"> ₹ Ruppee</option>
            </select>
        </div>
        </div>
    );
};

export default Currency;