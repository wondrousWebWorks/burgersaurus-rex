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
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

const card = elements.create('card', {style: style});
card.mount('#card-element');

// Realtime card element validation errors
card.addEventListener('change', event => {
    const errorDiv = document.querySelector('#card-errors');
    if (event.error) {
        const html = `
            <span class="icon" role="alert">
            <i class="fas fa-exclamation-triangle"></i>
            </span>
            <span class="open-sans">${event.error.message}</span>
        `;
        errorDiv.innerHTML = html;
    } else {
        errorDiv.textContent = '';
    }
});

// Handle payment form submit
const form = document.querySelector('#payment-form');
const submitButton = document.querySelector('#submit-button');
const loadingWrapper = document.querySelector('#loading-wrapper');

form.addEventListener('submit', event => {
    event.preventDefault();
    card.update({ 'disabled': true });
    submitButton.setAttribute('disabled', true);
    loadingWrapper.classList.toggle('opacity-full');
    const saveInfoCheckbox = document.querySelector('#id-save-info');
    const saveInfo = Boolean(saveInfoCheckbox.hasAttribute('checked'));
    console.log(saveInfo);
    const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    const postData = {
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    const  targetUrl = '/checkout/cache-checkout-data/';

    fetch(targetUrl, {
        method: "post",
        credentials: "same-origin",
        headers: {
            "X-CSRFToken": csrfToken,
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify(postData)
    }).then(response => {
        return response;
    }).then(data => {
        console.log("Data is ok", data);
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: form.full_name.value.trim(),
                    phone: form.phone_number.value.trim(),
                    email: form.email.value.trim(),
                    address:{
                        line1: form.street_address1.value.trim(),
                        line2: form.street_address2.value.trim(),
                        city: form.town_or_city.value.trim(),
                    }
                }
            },
            shipping: {
                name: form.full_name.value.trim(),
                phone: form.phone_number.value.trim(),
                address: {
                    line1: form.street_address1.value.trim(),
                    line2: form.street_address2.value.trim(),
                    city: form.town_or_city.value.trim(),
                    postal_code: form.postcode.value.trim(),
                }
            }
        }).then(result => {
            if (result.error) {
                const errorDiv = document.querySelector('#card-errors');
                const html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-exclamation-triangle"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                errorDiv.innerHTML = html;
                loadingWrapper.classList.toggle('opacity-full');
                card.update({ 'disabled': false });
                submitButton.setAttribute('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).catch(error => {
        console.log("Something went wrong!", error);
    });
});