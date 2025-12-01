document.addEventListener('DOMContentLoaded', function () {

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
            "::placeholder": { color: "#6c757d" }
        },
        invalid: {
            color: "#dc3545",
            iconColor: "#dc3545"
        }
    };

    // Create card element
    const card = elements.create("card", { style: style });

    // Mount card element
    card.mount("#card-element");

    // Handle realtime validation errors
    card.on('change', function(event) {
        const displayError = document.getElementById('card-errors');
        displayError.textContent = event.error ? event.error.message : '';
    });

    // Handle form submission
    const form = document.getElementById('payment-form');
    form.addEventListener('submit', function(ev) {
        ev.preventDefault();

        // Disable card input and submit button to prevent double submissions
        card.update({ 'disabled': true });
        document.getElementById('submit-button').disabled = true;

        stripe.confirmCardPayment(clientSecret, {
            payment_method: { card: card }
        }).then(function(result) {
            if (result.error) {
                // Show error to customer
                document.getElementById('card-errors').textContent = result.error.message;

                // Re-enable card input and submit button
                card.update({ 'disabled': false });
                document.getElementById('submit-button').disabled = false;

                // Redirect to payment declined page
                window.location.href = paymentDeclinedUrl;  
            } else {
                // Payment succeeded, submit the form
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    });

});
