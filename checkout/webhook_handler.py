from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Order, OrderLineItem
from products.models import Product

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle a generic/unknown/unexpected webhook event"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        Here you can create the order in your database if not already created
        """
        # Example: get payment info from event
        intent = event.data.object
        pid = intent.id
        # You can check if order exists, create order, send email, etc.
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """Handle payment failure webhook"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
