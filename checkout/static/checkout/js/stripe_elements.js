// ---------- Get Keys ----------
const stripePublicKey = document.getElementById('id_stripe_public_key').textContent.trim();
const clientSecret = document.getElementById('id_client_secret').textContent.trim();

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

form.addEventListener('submit', function(ev) {
    ev.preventDefault();

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
        } else {
            if (result.paymentIntent.status === "succeeded") {
                form.submit();
            }
        }
    });
});
