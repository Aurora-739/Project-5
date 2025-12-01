from django.urls import path
from . import views, webhooks

app_name = 'checkout'  # ← this is required for namespacing

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('success/<order_number>/', views.checkout_success, name='checkout_success'),
    path('webhook/', webhooks.webhook, name='webhook'),
    path('wh/', webhooks.webhook, name='webhook'),
    path('payment-declined/', views.payment_declined, name='payment_declined'),
]
