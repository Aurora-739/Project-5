document.addEventListener('DOMContentLoaded', function () {

    const stripePublicKey = JSON.parse(document.getElementById('id_stripe_public_key').textContent);
    const clientSecret = JSON.parse(document.getElementById('id_client_secret').textContent);

    const stripe = Stripe(stripePublicKey);
    const elements = stripe.elements();

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

    const card = elements.create("card", { style: style });
    card.mount("#card-element");

    card.on('change', function(event) {
        const displayError = document.getElementById('card-errors');
        displayError.textContent = event.error ? event.error.message : '';
    });

    const form = document.getElementById('payment-form');
    form.addEventListener('submit', function(ev) {
        ev.preventDefault();

        card.update({ 'disabled': true });
        document.getElementById('submit-button').disabled = true;

        // Optional metadata for testing
        let saveInfo = document.querySelector('#id-save-info') ? document.querySelector('#id-save-info').checked : false;
        let username = document.querySelector('#id-username') ? document.querySelector('#id-username').value : 'AnonymousUser';

        stripe.confirmCardPayment(clientSecret, {
            payment_method: { card: card }
        }).then(function(result) {
            if (result.error) {
                document.getElementById('card-errors').textContent = result.error.message;
                card.update({ 'disabled': false });
                document.getElementById('submit-button').disabled = false;

                // Redirect to declined page (optional)
                if (typeof paymentDeclinedUrl !== 'undefined') {
                    window.location.href = paymentDeclinedUrl;
                }
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    // Option 1: submit form to Django (for local testing)
                    form.submit();

                    // Option 2: skip form and rely on webhook
                    // window.location.href = '/checkout/success/';
                }
            }
        });
    });

});
