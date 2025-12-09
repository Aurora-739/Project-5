// ---------- Get Keys ----------
const stripePublicKey = JSON.parse(document.getElementById('id_stripe_public_key').textContent);
const clientSecret = JSON.parse(document.getElementById('id_client_secret').textContent);

// ---------- Initialise Stripe ----------
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();

// ---------- Styling ----------
const style = {
    base: {
        color: "#000",
        fontFamily: 'Arial, sans-serif',
        fontSize: '16px',
        '::placeholder': {
            color: '#888',
        },
    },
    invalid: {
        color: '#fa755a',
    },
};

// ---------- Create Card Element ----------
const card = elements.create('card', { style: style });
card.mount('#card-element');

// ---------- Handle Errors ----------
card.on('change', function (event) {
    const errorDiv = document.getElementById('card-errors');
    if (event.error) {
        errorDiv.textContent = event.error.message;
    } else {
        errorDiv.textContent = '';
    }
});

// ---------- Handle Form Submit ----------
const form = document.getElementById('payment-form');
const submitButton = document.getElementById('submit-button');
let isProcessing = false; 

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    
    // Prevent multiple submissions
    if (isProcessing) {
        return;
    }
    
    isProcessing = true;
    submitButton.disabled = true;
    submitButton.textContent = 'Processing...';

    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: form.full_name.value,
                email: form.email.value,
            }
        }
    }).then(function(result) {
        if (result.error) {
            document.getElementById('card-errors').textContent = result.error.message;
            // Re-enable button on error
            submitButton.disabled = false;
            submitButton.textContent = 'Place Order';
            isProcessing = false;
        } else {
            if (result.paymentIntent.status === "succeeded") {
                // Add client_secret to form before submitting
                const hiddenInput = document.createElement('input');
                hiddenInput.setAttribute('type', 'hidden');
                hiddenInput.setAttribute('name', 'client_secret');
                hiddenInput.setAttribute('value', clientSecret);
                form.appendChild(hiddenInput);
                
                form.submit();
            }
        }
    });
});
