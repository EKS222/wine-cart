import React, { useState } from 'react';
import axios from 'axios';

import './PaymentPrompt.css'; 

function PaymentPrompt() {
  const [phoneNumber, setPhoneNumber] = useState('');
  const [amount, setAmount] = useState('');

  const sendPaymentPrompt = async () => {
    try {
      //This is the actual  URL of the server
      const response = await axios.post('http://localhost:3000/callback', {
        phoneNumber,
        amount,
      });
     
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="mpesa-payment-form">
      <h2>M-Pesa Payment Prompt</h2>
      <form>
        <div className="input-container">
          <label htmlFor="phoneNumber">Phone Number:</label>
          <input
            type="text"
            id="phoneNumber"
            value={phoneNumber}
            onChange={(e) => setPhoneNumber(e.target.value)}
          />
        </div>
        <div className="input-container">
          <label htmlFor="amount">Amount (KES):</label>
          <input
            type="number"
            id="amount"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
          />
        </div>
        <button type="button" onClick={sendPaymentPrompt}>
          Send Payment Prompt
        </button>
      </form>
    </div>
  );
}

export default PaymentPrompt;