/*jshint esversion: 6 */

const stripePublicKey = document.querySelector('#stripe-public-key').innerText.slice(1, -1);
const clientSecret = document.querySelector('#client-secret').innerText.slice(1, -1);

const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();
const style = {
    base: {
        color: '#000',
        fontFamily: '"Open Sans", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        fontWeight: 'normal',
        '::placeholder': {
            color: '#aab7c4'
        },
        backgroundColor: 'white',
        padding: '1rem',
        border: 'none'
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
let card = elements.create('card', {style: style});
card.mount('#card-element');