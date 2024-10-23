import React from 'react';
const consumerKey = oGisXr1zX8IK7JTXOtaDf9TselAQXF6D;
const consumerSecret = zqBwgi960YIbklY8;
const callbackURL = 'http://localhost:3000/callback';


const axios = require('axios');

const paymentData = {
  amount: "1000",  
  phoneNumber: "0114212111"  
};

axios.post('http://localhost:5000/mpesa/payment', paymentData)
  .then(response => {
    console.log('Payment request initiated successfully:', response.data);
  })
  .catch(error => {
    console.error('Error initiating payment:', error);
  });