// Get keys from template
const stripePublicKey = JSON.parse(document.getElementById('id_stripe_public_key').textContent);
const clientSecret = JSON.parse(document.getElementById('id_client_secret').textContent);

const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();

// Style for the card element
const style = {
    base: {
        color: "#000",
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSize: "16px",
        "::placeholder": {
            color: "#6c757d"
        }
    },
    invalid: {
        color: "#dc3545",
        iconColor: "#dc3545"
    }
};

// Create card element
const card = elements.create("card", { style: style });

// Mount card element to div
card.mount("#card-element");

// Handle realtime validation errors
card.on('change', function(event) {
    const displayError = document.getElementById('card-errors');
    if (event.error) {
        displayError.textContent = event.error.message;
    } else {
        displayError.textContent = '';
    }
});

// Handle form submission
const form = document.getElementById('payment-form');
form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: document.getElementById('id_full_name').value,
                email: document.getElementById('id_email').value
            }
        }
    }).then(function(result) {
        if (result.error) {
            // Show error to your customer
            document.getElementById('card-errors').textContent = result.error.message;
        } else {
            // Payment succeeded, submit form
            form.submit();
        }
    });
});
